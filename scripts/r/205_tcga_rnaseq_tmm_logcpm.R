# =======================================================
# 205 — TCGA RNA-seq TMM log-CPM normalization
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
# Define input and output artifact paths
# =======================================================

expression_dir <- file.path(
  project_root,
  "data/interim/expression"
)

counts_h5_path <- file.path(
  expression_dir,
  "tcga_primary_tumor_rnaseq_program_discovery_filtered_raw_counts.h5"
)

gene_metadata_path <- file.path(
  expression_dir,
  "tcga_primary_tumor_rnaseq_program_discovery_filtered_gene_metadata.csv"
)

sample_metadata_path <- file.path(
  expression_dir,
  "tcga_primary_tumor_rnaseq_program_discovery_sample_metadata.csv"
)

tmm_logcpm_h5_path <- file.path(
  expression_dir,
  "tcga_primary_tumor_rnaseq_program_discovery_tmm_logcpm.h5"
)

tmm_factors_path <- file.path(
  expression_dir,
  "tcga_primary_tumor_rnaseq_program_discovery_tmm_factors.csv"
)

session_info_path <- file.path(
  expression_dir,
  "tcga_primary_tumor_rnaseq_program_discovery_tmm_session_info.txt"
)


# =======================================================
# Load RNA-seq exchange metadata
# =======================================================

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


# =======================================================
# Load filtered counts in genes-by-samples orientation
# =======================================================

counts <- t(
  h5read(
    counts_h5_path,
    "counts"
  )
)

expected_dimensions <- c(
  nrow(gene_metadata),
  nrow(sample_metadata)
)

if (!identical(dim(counts), expected_dimensions)) {
  stop(
    "The count-matrix orientation does not match ",
    "the gene and sample metadata."
  )
}

rownames(counts) <- gene_metadata$gene_id
colnames(counts) <- sample_metadata$case_submitter_id


# =======================================================
# Apply TMM library normalization
# =======================================================

dge <- DGEList(
  counts = counts,
  genes = gene_metadata,
  samples = sample_metadata
)

rm(counts)
gc()

dge <- calcNormFactors(
  dge,
  method = "TMM"
)

summary(dge$samples$norm.factors)


# =======================================================
# Calculate TMM-normalized log-CPM
# =======================================================

rna_tmm_logcpm <- cpm(
  dge,
  log = TRUE,
  prior.count = 2,
  normalized.lib.sizes = TRUE
)

dim(rna_tmm_logcpm)
summary(as.vector(rna_tmm_logcpm))


# =======================================================
# Write TMM-normalized log-CPM to HDF5
# =======================================================

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


# =======================================================
# Write TMM normalization factors
# =======================================================

tmm_factors <- dge$samples

tmm_factors$effective_library_size <- (
  tmm_factors$lib.size
  * tmm_factors$norm.factors
)

write.csv(
  tmm_factors,
  tmm_factors_path,
  row.names = FALSE
)


# =======================================================
# Verify written normalization artifacts
# =======================================================

written_tmm_factors <- read.csv(
  tmm_factors_path,
  stringsAsFactors = FALSE,
  check.names = FALSE
)

logcpm_subset <- h5read(
  tmm_logcpm_h5_path,
  "logcpm",
  index = list(1:5, 1:5),
  native = TRUE
)

verification_summary <- list(
  logcpm_structure = h5ls(tmm_logcpm_h5_path),
  orientation = h5readAttributes(
    tmm_logcpm_h5_path,
    "logcpm"
  )$orientation,
  subset_matches_memory = isTRUE(
    all.equal(
      unname(logcpm_subset),
      unname(rna_tmm_logcpm[1:5, 1:5]),
      tolerance = 0
    )
  ),
  tmm_factor_rows = nrow(written_tmm_factors),
  tmm_factor_columns = ncol(written_tmm_factors),
  factors_match_memory = isTRUE(
    all.equal(
      written_tmm_factors$norm.factors,
      dge$samples$norm.factors,
      tolerance = 1e-12
    )
  )
)

verification_summary


# =======================================================
# Record R session information
# =======================================================

writeLines(
  capture.output(sessionInfo()),
  session_info_path
)

session_info_path