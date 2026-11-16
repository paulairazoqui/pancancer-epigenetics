# =======================================================
# 800 — CPTAC3 RNA-seq TMM log-CPM normalization
# =======================================================


# =======================================================
# Resolve project root from script location
# =======================================================

get_script_path <- function() {
  command_args <- commandArgs(trailingOnly = FALSE)
  file_argument <- grep(
    "^--file=",
    command_args,
    value = TRUE
  )

  if (length(file_argument) == 1) {
    return(
      normalizePath(
        sub("^--file=", "", file_argument),
        winslash = "/",
        mustWork = TRUE
      )
    )
  }

  if (
    requireNamespace("rstudioapi", quietly = TRUE) &&
    rstudioapi::isAvailable()
  ) {
    active_path <- rstudioapi::getSourceEditorContext()$path

    if (nzchar(active_path)) {
      return(
        normalizePath(
          active_path,
          winslash = "/",
          mustWork = TRUE
        )
      )
    }
  }

  stop("Could not resolve the current R script path.")
}

script_path <- get_script_path()

project_root <- normalizePath(
  file.path(
    dirname(script_path),
    "..",
    ".."
  ),
  winslash = "/",
  mustWork = TRUE
)

rm(get_script_path, script_path)

project_root


# =======================================================
# Check and load required packages
# =======================================================

required_packages <- c(
  "edgeR",
  "rhdf5"
)

package_status <- vapply(
  required_packages,
  requireNamespace,
  logical(1),
  quietly = TRUE
)

if (any(!package_status)) {
  stop(
    "Missing required packages: ",
    paste(
      names(package_status)[!package_status],
      collapse = ", "
    )
  )
}

suppressPackageStartupMessages({
  library(edgeR)
  library(rhdf5)
})

# =======================================================
# Load CPTAC-3 RNA-seq counts and metadata
# =======================================================

expression_dir <- file.path(
  project_root,
  "data/interim/expression"
)

counts_h5_path <- file.path(
  expression_dir,
  "800_cptac3_protein_coding_raw_counts.h5"
)

gene_metadata_path <- file.path(
  expression_dir,
  "800_cptac3_protein_coding_gene_metadata.csv"
)

sample_metadata_path <- file.path(
  expression_dir,
  "800_cptac3_sample_metadata.csv"
)

gene_metadata <- read.csv(
  gene_metadata_path,
  stringsAsFactors = FALSE,
  check.names = FALSE
)

sample_metadata <- read.csv(
  sample_metadata_path,
  stringsAsFactors = FALSE,
  check.names = FALSE
)

# The Python HDF5 layout is transposed by rhdf5 on import.
counts <- t(h5read(counts_h5_path, "counts"))

expected_dimensions <- c(
  nrow(gene_metadata),
  nrow(sample_metadata)
)

if (!identical(dim(counts), expected_dimensions)) {
  stop("Count matrix orientation does not match metadata.")
}

rownames(counts) <- gene_metadata$ensembl_gene_id
colnames(counts) <- sample_metadata$file_id

cat("Count matrix:", dim(counts), "\n")
cat("Storage mode:", storage.mode(counts), "\n")
cat("Cancer lineages:", length(unique(sample_metadata$tcga_lineage)), "\n")


# =======================================================
# Filter genes and estimate TMM normalization factors
# =======================================================

lineage_group <- factor(sample_metadata$tcga_lineage)

dge_full <- DGEList(
  counts = counts,
  genes = gene_metadata,
  samples = sample_metadata,
  group = lineage_group
)

# Filtering defines the TMM reference, not the final scoring genes.
keep <- filterByExpr(
  dge_full,
  group = lineage_group
)

dge_tmm <- dge_full[keep, , keep.lib.sizes = FALSE]

dge_tmm <- normLibSizes(
  dge_tmm,
  method = "TMM"
)

cat("Protein-coding genes:", nrow(dge_full), "\n")
cat("Genes retained for TMM:", nrow(dge_tmm), "\n")
cat("Samples:", ncol(dge_tmm), "\n")

summary(dge_tmm$samples$norm.factors)


# =======================================================
# Calculate TMM-normalized logCPM for frozen genes
# =======================================================

reference_path <- file.path(
  project_root,
  "data/processed/consensus_programs",
  "400_cross_system_shared_gene_universe.csv"
)

shared_genes <- read.csv(
  reference_path,
  stringsAsFactors = FALSE,
  check.names = FALSE
)

frozen_gene_ids <- sub(
  "\\.[0-9]+$",
  "",
  shared_genes$tumor_gene_id
)

if (
  anyDuplicated(frozen_gene_ids) ||
  anyNA(match(frozen_gene_ids, rownames(dge_full)))
) {
  stop("Frozen gene identifiers cannot be uniquely aligned.")
}

# Preserve effective library sizes from broad-gene TMM estimation.
effective_library_sizes <- (
  dge_tmm$samples$lib.size *
    dge_tmm$samples$norm.factors
)

rna_tmm_logcpm <- cpm(
  dge_full$counts[frozen_gene_ids, , drop = FALSE],
  lib.size = effective_library_sizes,
  log = TRUE,
  prior.count = 2
)

frozen_gene_indices <- match(
  frozen_gene_ids,
  rownames(dge_full)
)

cat("Frozen genes:", length(frozen_gene_ids), "\n")
cat("Frozen genes passing filter:", sum(keep[frozen_gene_indices]), "\n")
cat("Normalized matrix:", dim(rna_tmm_logcpm), "\n")
cat("Finite logCPM values:", all(is.finite(rna_tmm_logcpm)), "\n")


# =======================================================
# Save normalized expression and TMM metadata
# =======================================================

tmm_logcpm_h5_path <- file.path(
  expression_dir,
  "800_cptac3_frozen_genes_tmm_logcpm.h5"
)

tmm_factors_path <- file.path(
  expression_dir,
  "800_cptac3_tmm_factors.csv"
)

session_info_path <- file.path(
  expression_dir,
  "800_cptac3_tmm_session_info.txt"
)

if (file.exists(tmm_logcpm_h5_path)) {
  file.remove(tmm_logcpm_h5_path)
}

h5write(
  rna_tmm_logcpm,
  file = tmm_logcpm_h5_path,
  name = "logcpm",
  native = TRUE
)

h5_file <- H5Fopen(tmm_logcpm_h5_path)
logcpm_dataset <- H5Dopen(h5_file, "logcpm")

h5writeAttribute(
  "genes_x_samples",
  logcpm_dataset,
  "orientation"
)

H5Dclose(logcpm_dataset)
H5Fclose(h5_file)

tmm_factors <- dge_tmm$samples
tmm_factors$effective_library_size <- effective_library_sizes

write.csv(
  tmm_factors,
  tmm_factors_path,
  row.names = FALSE
)

writeLines(
  capture.output(sessionInfo()),
  session_info_path
)

cat("Normalized matrix saved:", dim(rna_tmm_logcpm), "\n")
cat("TMM factor records:", nrow(tmm_factors), "\n")
cat("R session information saved.\n")