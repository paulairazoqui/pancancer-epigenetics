# =============================================================================
# Export SeSAMe HM450 hg38 annotation for notebook 451
# =============================================================================
#
# Required environment:
#   R 4.6.1
#   Bioconductor 3.23
#   sesameData 1.30.0
#
# Run from the pancancer-epigenetics repository root.
#
# This script exports a deterministic biological annotation resource for the
# frozen HM450 CpG universe used in Phase 4B notebook 451.
# =============================================================================

repo_root <- normalizePath(
  getwd(),
  winslash = "/",
  mustWork = TRUE
)

if (!file.exists(
  file.path(repo_root, "config", "raw_data_registry.json")
)) {
  stop(
    "Run this script from the pancancer-epigenetics repository root."
  )
}

script_relative_path <- paste(
  "scripts",
  "phase4b",
  "export_sesamedata_hm450_hg38_annotation.R",
  sep = "/"
)

required_namespaces <- c(
  "BiocManager",
  "sesameData",
  "ExperimentHub",
  "GenomeInfoDb",
  "GenomicRanges",
  "S4Vectors",
  "BiocGenerics"
)

namespace_available <- vapply(
  required_namespaces,
  requireNamespace,
  quietly = TRUE,
  FUN.VALUE = logical(1)
)

if (!all(namespace_available)) {
  stop(
    "Missing required R packages: ",
    paste(
      required_namespaces[!namespace_available],
      collapse = ", "
    )
  )
}

if (as.character(getRversion()) != "4.6.1") {
  stop("R 4.6.1 is required.")
}

if (as.character(BiocManager::version()) != "3.23") {
  stop("Bioconductor 3.23 is required.")
}

if (as.character(packageVersion("sesameData")) != "1.30.0") {
  stop("sesameData 1.30.0 is required.")
}

library(sesameData)

validated_platform <- as.character(
  sesameData_check_platform("HM450")
)

validated_genome <- as.character(
  sesameData_check_genome("hg38", "HM450")
)

if (validated_platform != "HM450") {
  stop("Unexpected sesameData platform validation result.")
}

if (validated_genome != "hg38") {
  stop("Unexpected sesameData genome validation result.")
}

cat("Repository root:", repo_root, "\n")
cat("R version:", as.character(getRversion()), "\n")
cat("Bioconductor version:", as.character(BiocManager::version()), "\n")
cat("sesameData version:", as.character(packageVersion("sesameData")), "\n")
cat("Validated platform:", validated_platform, "\n")
cat("Validated genome:", validated_genome, "\n\n")


# =============================================================================
# Freeze and cache exact sesameData annotation resources
# =============================================================================

frozen_sesame_resources <- data.frame(
  Title = c(
    "HM450.address",
    "genomeInfo.hg38"
  ),
  expected_EHID = c(
    "EH7317",
    "EH8558"
  ),
  expected_VERSION = c(
    "1.13.1",
    "1.21.1"
  ),
  expected_SOURCE_VERSION = c(
    "2022-01-23",
    "2024-01-11"
  ),
  stringsAsFactors = FALSE
)

sesame_catalog <- sesameDataList(
  full = TRUE
)

resource_rows <- match(
  frozen_sesame_resources$Title,
  sesame_catalog$Title
)

if (anyNA(resource_rows)) {
  stop(
    "At least one frozen sesameData resource is absent from the catalog."
  )
}

observed_sesame_resources <- sesame_catalog[
  resource_rows,
  c(
    "EHID",
    "VERSION",
    "IN_USE",
    "Title",
    "Genome",
    "SourceVersion",
    "RDataClass",
    "RDataPath"
  )
]

if (!all(
  observed_sesame_resources$EHID ==
  frozen_sesame_resources$expected_EHID
)) {
  stop("Unexpected ExperimentHub resource identity.")
}

if (!all(
  observed_sesame_resources$VERSION ==
  frozen_sesame_resources$expected_VERSION
)) {
  stop("Unexpected sesameData resource version.")
}

if (!all(
  as.character(observed_sesame_resources$SourceVersion) ==
  frozen_sesame_resources$expected_SOURCE_VERSION
)) {
  stop("Unexpected sesameData source-resource version.")
}

if (!all(observed_sesame_resources$IN_USE)) {
  stop("At least one frozen sesameData resource is not active.")
}

# =============================================================================
# Cache frozen sesameData annotation resources non-interactively
# =============================================================================

ExperimentHub::setExperimentHubOption(
  "ASK",
  FALSE
)

cat(
  "ExperimentHub cache:",
  ExperimentHub::getExperimentHubOption("CACHE"),
  "\n"
)

sesameDataCache(
  frozen_sesame_resources$Title
)

cat(
  "Frozen sesameData resources cached successfully.\n\n"
)

print(
  as.data.frame(observed_sesame_resources),
  row.names = FALSE
)




# =============================================================================
# Build and validate frozen HM450 hg38 manifest
# =============================================================================

hm450_hg38_manifest <- sesameData_getManifestGRanges(
  platform = "HM450",
  genome = "hg38"
)

if (!inherits(hm450_hg38_manifest, "GRanges")) {
  stop("HM450 hg38 manifest is not a GRanges object.")
}

manifest_probe_ids <- names(hm450_hg38_manifest)

if (length(hm450_hg38_manifest) != 485545L) {
  stop("Unexpected number of frozen HM450 manifest loci.")
}

if (is.null(manifest_probe_ids)) {
  stop("HM450 manifest does not preserve probe identifiers as GRanges names.")
}

if (anyDuplicated(manifest_probe_ids) > 0) {
  stop("HM450 manifest contains duplicated probe identifiers.")
}

cat("Manifest class:", class(hm450_hg38_manifest)[1], "\n")
cat("Manifest loci:", length(hm450_hg38_manifest), "\n")
cat(
  "Requested genome build:",
  validated_genome,
  "\n"
)
cat(
  "Seqlevels:",
  length(GenomeInfoDb::seqlevels(hm450_hg38_manifest)),
  "\n"
)
cat(
  "Probe IDs stored as GRanges names:",
  !is.null(manifest_probe_ids),
  "\n"
)

if (!is.null(manifest_probe_ids)) {
  cat(
    "Unique probe IDs:",
    length(unique(manifest_probe_ids)),
    "\n"
  )
  cat(
    "Duplicated probe IDs:",
    sum(duplicated(manifest_probe_ids)),
    "\n"
  )
  cat(
    "CpG-style probe IDs:",
    sum(grepl("^cg", manifest_probe_ids)),
    "\n"
  )
}

cat(
  "Metadata columns:",
  paste(
    names(S4Vectors::mcols(hm450_hg38_manifest)),
    collapse = ", "
  ),
  "\n\n"
)


# =============================================================================
# Load and validate frozen hg38 transcript annotation
# =============================================================================

hg38_transcripts <- sesameData_getTxnGRanges(
  genome = "hg38"
)

if (!inherits(hg38_transcripts, "GRanges")) {
  stop("hg38 transcript annotation is not a GRanges object.")
}

cat(
  "Transcript annotation class:",
  class(hg38_transcripts)[1],
  "\n"
)

cat(
  "Transcript records:",
  length(hg38_transcripts),
  "\n"
)

cat(
  "Seqlevels:",
  length(
    GenomeInfoDb::seqlevels(hg38_transcripts)
  ),
  "\n"
)

cat(
  "Metadata columns:",
  paste(
    names(
      S4Vectors::mcols(hg38_transcripts)
    ),
    collapse = ", "
  ),
  "\n"
)

cat(
  "Unique transcript names:",
  length(
    unique(names(hg38_transcripts))
  ),
  "\n"
)

cat(
  "Duplicated transcript names:",
  sum(
    duplicated(names(hg38_transcripts))
  ),
  "\n\n"
)


# =============================================================================
# Audit hg38 transcript-to-gene annotation consistency
# =============================================================================

transcript_annotation <- as.data.frame(
  hg38_transcripts
)

transcript_annotation$transcript_id <- names(
  hg38_transcripts
)

transcript_annotation$gene_id_base <- sub(
  "\\.[0-9]+$",
  "",
  transcript_annotation$gene_id
)

if (anyNA(transcript_annotation$gene_id)) {
  stop("Transcript annotation contains missing gene identifiers.")
}

if (anyNA(transcript_annotation$gene_name)) {
  stop("Transcript annotation contains missing gene symbols.")
}

gene_locus_key <- paste(
  transcript_annotation$seqnames,
  transcript_annotation$strand,
  sep = "|"
)

gene_locus_counts <- tapply(
  gene_locus_key,
  transcript_annotation$gene_id_base,
  function(values) {
    length(unique(values))
  }
)

protein_coding_mask <- (
  transcript_annotation$gene_type == "protein_coding"
)

protein_coding_gene_ids <- unique(
  transcript_annotation$gene_id_base[
    protein_coding_mask
  ]
)

if (nrow(transcript_annotation) != 232117L) {
  stop("Unexpected number of frozen hg38 transcript records.")
}

if (length(unique(transcript_annotation$gene_id_base)) != 60660L) {
  stop("Unexpected number of hg38 Ensembl gene identifiers.")
}

if (sum(protein_coding_mask) != 157222L) {
  stop("Unexpected number of protein-coding transcript records.")
}

if (length(protein_coding_gene_ids) != 19962L) {
  stop("Unexpected number of protein-coding genes.")
}

if (any(gene_locus_counts > 1L)) {
  stop("At least one gene is represented on multiple chromosome/strand loci.")
}

cat(
  "Transcript records:",
  nrow(transcript_annotation),
  "\n"
)

cat(
  "Unique Ensembl gene IDs:",
  length(
    unique(transcript_annotation$gene_id_base)
  ),
  "\n"
)

cat(
  "Protein-coding transcript records:",
  sum(protein_coding_mask),
  "\n"
)

cat(
  "Unique protein-coding genes:",
  length(protein_coding_gene_ids),
  "\n"
)

cat(
  "Genes represented on >1 chromosome/strand locus:",
  sum(gene_locus_counts > 1),
  "\n"
)

cat(
  "Missing gene symbols:",
  sum(is.na(transcript_annotation$gene_name)),
  "\n"
)

cat(
  "Missing gene IDs:",
  sum(is.na(transcript_annotation$gene_id)),
  "\n"
)





# =============================================================================
# Freeze promoter definition and construct transcript-level promoter intervals
# =============================================================================

PROMOTER_UPSTREAM_BP <- 1500L
PROMOTER_DOWNSTREAM_BP <- 1500L

if (!requireNamespace("GenomicRanges", quietly = TRUE)) {
  stop("GenomicRanges is required.")
}

hg38_transcript_promoters <- GenomicRanges::promoters(
  hg38_transcripts,
  upstream = PROMOTER_UPSTREAM_BP,
  downstream = PROMOTER_DOWNSTREAM_BP
)

if (length(hg38_transcript_promoters) != length(hg38_transcripts)) {
  stop(
    "Transcript and promoter annotations do not have one-to-one correspondence."
  )
}

if (!identical(
  names(hg38_transcript_promoters),
  names(hg38_transcripts)
)) {
  stop(
    "Transcript identities were not preserved during promoter construction."
  )
}

cat(
  "Promoter upstream bp:",
  PROMOTER_UPSTREAM_BP,
  "\n"
)

cat(
  "Promoter downstream bp:",
  PROMOTER_DOWNSTREAM_BP,
  "\n"
)

cat(
  "Transcript promoters:",
  length(hg38_transcript_promoters),
  "\n"
)

cat(
  "Unique promoter transcript IDs:",
  length(unique(names(hg38_transcript_promoters))),
  "\n"
)

cat(
  "Promoter/transcript identity preserved:",
  identical(
    names(hg38_transcript_promoters),
    names(hg38_transcripts)
  ),
  "\n"
)


# =============================================================================
# Restrict transcript and promoter annotations to protein-coding genes
# =============================================================================

protein_coding_transcript_mask <- (
  S4Vectors::mcols(hg38_transcripts)$gene_type == "protein_coding"
)

hg38_protein_coding_transcripts <- hg38_transcripts[
  protein_coding_transcript_mask
]

hg38_protein_coding_promoters <- hg38_transcript_promoters[
  protein_coding_transcript_mask
]

if (length(hg38_protein_coding_transcripts) !=
    length(hg38_protein_coding_promoters)) {
  stop(
    "Protein-coding transcript and promoter annotations are misaligned."
  )
}

if (!identical(
  names(hg38_protein_coding_transcripts),
  names(hg38_protein_coding_promoters)
)) {
  stop(
    "Protein-coding transcript identities are not preserved."
  )
}

protein_coding_gene_ids_base <- sub(
  "\\.[0-9]+$",
  "",
  S4Vectors::mcols(
    hg38_protein_coding_transcripts
  )$gene_id
)

cat(
  "Protein-coding transcript records:",
  length(hg38_protein_coding_transcripts),
  "\n"
)

cat(
  "Unique protein-coding genes:",
  length(unique(protein_coding_gene_ids_base)),
  "\n"
)

cat(
  "Protein-coding promoters:",
  length(hg38_protein_coding_promoters),
  "\n"
)

cat(
  "Transcript/promoter identity preserved:",
  identical(
    names(hg38_protein_coding_transcripts),
    names(hg38_protein_coding_promoters)
  ),
  "\n"
)

cat(
  "Missing protein-coding gene IDs:",
  sum(
    is.na(
      S4Vectors::mcols(
        hg38_protein_coding_transcripts
      )$gene_id
    )
  ),
  "\n"
)

cat(
  "Missing protein-coding gene symbols:",
  sum(
    is.na(
      S4Vectors::mcols(
        hg38_protein_coding_transcripts
      )$gene_name
    )
  ),
  "\n"
)





# =============================================================================
# Restrict HM450 manifest to CpG probes
# =============================================================================

hm450_cpg_mask <- grepl(
  "^cg[0-9]{8}$",
  names(hm450_hg38_manifest)
)

hm450_cpg_manifest <- hm450_hg38_manifest[
  hm450_cpg_mask
]

if (length(hm450_cpg_manifest) != 482389L) {
  stop("Unexpected number of HM450 CpG probes.")
}

if (anyDuplicated(names(hm450_cpg_manifest)) > 0) {
  stop("HM450 CpG manifest contains duplicated probe identifiers.")
}

if (!all(
  grepl("^cg[0-9]{8}$", names(hm450_cpg_manifest))
)) {
  stop("Non-CpG probe identifiers remain in the CpG manifest.")
}

cat(
  "Complete HM450 manifest loci:",
  length(hm450_hg38_manifest),
  "\n"
)

cat(
  "HM450 CpG probes:",
  length(hm450_cpg_manifest),
  "\n"
)

cat(
  "Excluded non-CpG probes:",
  length(hm450_hg38_manifest) -
    length(hm450_cpg_manifest),
  "\n"
)

cat(
  "Unique CpG probe IDs:",
  length(unique(names(hm450_cpg_manifest))),
  "\n"
)

cat(
  "Duplicated CpG probe IDs:",
  sum(duplicated(names(hm450_cpg_manifest))),
  "\n"
)

cat(
  "CpG seqlevels:",
  length(
    GenomeInfoDb::seqlevels(hm450_cpg_manifest)
  ),
  "\n"
)



# =============================================================================
# Map HM450 CpGs to protein-coding transcript promoters
# =============================================================================

promoter_hits <- GenomicRanges::findOverlaps(
  hm450_cpg_manifest,
  hg38_protein_coding_promoters,
  ignore.strand = TRUE
)

promoter_query_index <- S4Vectors::queryHits(
  promoter_hits
)

promoter_subject_index <- S4Vectors::subjectHits(
  promoter_hits
)

promoter_cpg_ranges <- hm450_cpg_manifest[
  promoter_query_index
]

promoter_transcript_ranges <- hg38_protein_coding_promoters[
  promoter_subject_index
]

promoter_annotation <- data.frame(
  probe_id = names(promoter_cpg_ranges),
  cpg_chr = as.character(
    GenomicRanges::seqnames(promoter_cpg_ranges)
  ),
  cpg_start = BiocGenerics::start(
    promoter_cpg_ranges
  ),
  cpg_end = BiocGenerics::end(
    promoter_cpg_ranges
  ),
  transcript_id = names(
    promoter_transcript_ranges
  ),
  gene_id = S4Vectors::mcols(
    promoter_transcript_ranges
  )$gene_id,
  gene_name = S4Vectors::mcols(
    promoter_transcript_ranges
  )$gene_name,
  promoter_chr = as.character(
    GenomicRanges::seqnames(promoter_transcript_ranges)
  ),
  promoter_start = BiocGenerics::start(
    promoter_transcript_ranges
  ),
  promoter_end = BiocGenerics::end(
    promoter_transcript_ranges
  ),
  stringsAsFactors = FALSE
)

promoter_annotation$gene_id_base <- sub(
  "\\.[0-9]+$",
  "",
  promoter_annotation$gene_id
)

if (anyNA(promoter_annotation$probe_id)) {
  stop("Promoter annotation contains missing CpG identifiers.")
}

if (anyNA(promoter_annotation$gene_id_base)) {
  stop("Promoter annotation contains missing gene identifiers.")
}

promoter_cpg_gene_pairs <- unique(
  promoter_annotation[
    ,
    c(
      "probe_id",
      "gene_id_base"
    )
  ]
)

promoter_gene_counts_per_cpg <- table(
  promoter_cpg_gene_pairs$probe_id
)

cat(
  "Transcript-level promoter overlaps:",
  nrow(promoter_annotation),
  "\n"
)

cat(
  "CpGs with >=1 promoter overlap:",
  length(unique(promoter_annotation$probe_id)),
  "\n"
)

cat(
  "Unique promoter-associated genes:",
  length(unique(promoter_annotation$gene_id_base)),
  "\n"
)

cat(
  "Unique CpG-gene promoter pairs:",
  nrow(promoter_cpg_gene_pairs),
  "\n"
)

cat(
  "CpGs mapping to >1 promoter-associated gene:",
  sum(promoter_gene_counts_per_cpg > 1),
  "\n"
)


# =============================================================================
# Map HM450 CpGs to protein-coding transcript intervals
# =============================================================================

transcript_hits <- GenomicRanges::findOverlaps(
  hm450_cpg_manifest,
  hg38_protein_coding_transcripts,
  ignore.strand = TRUE
)

transcript_query_index <- S4Vectors::queryHits(
  transcript_hits
)

transcript_subject_index <- S4Vectors::subjectHits(
  transcript_hits
)

genic_cpg_ranges <- hm450_cpg_manifest[
  transcript_query_index
]

genic_transcript_ranges <- hg38_protein_coding_transcripts[
  transcript_subject_index
]

genic_annotation <- data.frame(
  probe_id = names(genic_cpg_ranges),
  cpg_chr = as.character(
    GenomicRanges::seqnames(genic_cpg_ranges)
  ),
  cpg_start = BiocGenerics::start(
    genic_cpg_ranges
  ),
  cpg_end = BiocGenerics::end(
    genic_cpg_ranges
  ),
  transcript_id = names(
    genic_transcript_ranges
  ),
  gene_id = S4Vectors::mcols(
    genic_transcript_ranges
  )$gene_id,
  gene_name = S4Vectors::mcols(
    genic_transcript_ranges
  )$gene_name,
  transcript_chr = as.character(
    GenomicRanges::seqnames(genic_transcript_ranges)
  ),
  transcript_start = BiocGenerics::start(
    genic_transcript_ranges
  ),
  transcript_end = BiocGenerics::end(
    genic_transcript_ranges
  ),
  stringsAsFactors = FALSE
)

genic_annotation$gene_id_base <- sub(
  "\\.[0-9]+$",
  "",
  genic_annotation$gene_id
)

if (anyNA(genic_annotation$probe_id)) {
  stop("Genic annotation contains missing CpG identifiers.")
}

if (anyNA(genic_annotation$gene_id_base)) {
  stop("Genic annotation contains missing gene identifiers.")
}

genic_cpg_gene_pairs <- unique(
  genic_annotation[
    ,
    c(
      "probe_id",
      "gene_id_base"
    )
  ]
)

genic_gene_counts_per_cpg <- table(
  genic_cpg_gene_pairs$probe_id
)

cat(
  "Transcript-level genic overlaps:",
  nrow(genic_annotation),
  "\n"
)

cat(
  "CpGs with >=1 genic overlap:",
  length(unique(genic_annotation$probe_id)),
  "\n"
)

cat(
  "Unique genic-associated genes:",
  length(unique(genic_annotation$gene_id_base)),
  "\n"
)

cat(
  "Unique CpG-gene genic pairs:",
  nrow(genic_cpg_gene_pairs),
  "\n"
)

cat(
  "CpGs mapping to >1 genic-associated gene:",
  sum(genic_gene_counts_per_cpg > 1),
  "\n"
)


# =============================================================================
# Construct unique CpG-gene regulatory annotation
# =============================================================================

protein_coding_gene_lookup <- unique(
  data.frame(
    gene_id_base = protein_coding_gene_ids_base,
    gene_id = S4Vectors::mcols(
      hg38_protein_coding_transcripts
    )$gene_id,
    gene_name = S4Vectors::mcols(
      hg38_protein_coding_transcripts
    )$gene_name,
    stringsAsFactors = FALSE
  )
)

if (anyDuplicated(protein_coding_gene_lookup$gene_id_base) > 0) {
  stop(
    "Protein-coding Ensembl gene IDs do not map uniquely to gene metadata."
  )
}

hm450_cpg_lookup <- data.frame(
  probe_id = names(hm450_cpg_manifest),
  cpg_chr = as.character(
    GenomicRanges::seqnames(hm450_cpg_manifest)
  ),
  cpg_start = BiocGenerics::start(
    hm450_cpg_manifest
  ),
  cpg_end = BiocGenerics::end(
    hm450_cpg_manifest
  ),
  stringsAsFactors = FALSE
)

if (anyDuplicated(hm450_cpg_lookup$probe_id) > 0) {
  stop("HM450 CpG coordinate lookup contains duplicated probe IDs.")
}

promoter_pair_summary <- aggregate(
  transcript_id ~ probe_id + gene_id_base,
  data = promoter_annotation,
  FUN = function(values) {
    length(unique(values))
  }
)

names(promoter_pair_summary)[
  names(promoter_pair_summary) == "transcript_id"
] <- "promoter_transcript_count"

genic_pair_summary <- aggregate(
  transcript_id ~ probe_id + gene_id_base,
  data = genic_annotation,
  FUN = function(values) {
    length(unique(values))
  }
)

names(genic_pair_summary)[
  names(genic_pair_summary) == "transcript_id"
] <- "genic_transcript_count"

cpg_gene_regulatory_annotation <- merge(
  promoter_pair_summary,
  genic_pair_summary,
  by = c(
    "probe_id",
    "gene_id_base"
  ),
  all = TRUE,
  sort = FALSE
)

cpg_gene_regulatory_annotation$promoter_associated <- !is.na(
  cpg_gene_regulatory_annotation$promoter_transcript_count
)

cpg_gene_regulatory_annotation$transcript_associated <- !is.na(
  cpg_gene_regulatory_annotation$genic_transcript_count
)

cpg_gene_regulatory_annotation$promoter_transcript_count[
  is.na(
    cpg_gene_regulatory_annotation$promoter_transcript_count
  )
] <- 0L

cpg_gene_regulatory_annotation$genic_transcript_count[
  is.na(
    cpg_gene_regulatory_annotation$genic_transcript_count
  )
] <- 0L

cpg_gene_regulatory_annotation <- merge(
  cpg_gene_regulatory_annotation,
  hm450_cpg_lookup,
  by = "probe_id",
  all.x = TRUE,
  sort = FALSE
)

cpg_gene_regulatory_annotation <- merge(
  cpg_gene_regulatory_annotation,
  protein_coding_gene_lookup,
  by = "gene_id_base",
  all.x = TRUE,
  sort = FALSE
)

if (anyNA(cpg_gene_regulatory_annotation$cpg_chr)) {
  stop("At least one CpG-gene pair lacks HM450 genomic coordinates.")
}

if (anyNA(cpg_gene_regulatory_annotation$gene_name)) {
  stop("At least one CpG-gene pair lacks protein-coding gene metadata.")
}

cpg_gene_regulatory_annotation <- cpg_gene_regulatory_annotation[
  order(
    cpg_gene_regulatory_annotation$probe_id,
    cpg_gene_regulatory_annotation$gene_id_base
  ),
]

row.names(cpg_gene_regulatory_annotation) <- NULL

cat(
  "Unique CpG-gene regulatory pairs:",
  nrow(cpg_gene_regulatory_annotation),
  "\n"
)

cat(
  "Unique annotated CpGs:",
  length(
    unique(cpg_gene_regulatory_annotation$probe_id)
  ),
  "\n"
)

cat(
  "Unique annotated genes:",
  length(
    unique(cpg_gene_regulatory_annotation$gene_id_base)
  ),
  "\n"
)

cat(
  "Promoter-associated pairs:",
  sum(
    cpg_gene_regulatory_annotation$promoter_associated
  ),
  "\n"
)

cat(
  "Transcript-associated pairs:",
  sum(
    cpg_gene_regulatory_annotation$transcript_associated
  ),
  "\n"
)

cat(
  "Promoter + transcript-associated pairs:",
  sum(
    cpg_gene_regulatory_annotation$promoter_associated &
      cpg_gene_regulatory_annotation$transcript_associated
  ),
  "\n"
)

cat(
  "Promoter-only pairs:",
  sum(
    cpg_gene_regulatory_annotation$promoter_associated &
      !cpg_gene_regulatory_annotation$transcript_associated
  ),
  "\n"
)

cat(
  "Transcript-only pairs:",
  sum(
    !cpg_gene_regulatory_annotation$promoter_associated &
      cpg_gene_regulatory_annotation$transcript_associated
  ),
  "\n"
)


# =============================================================================
# Construct CpG-level protein-coding annotation coverage
# =============================================================================

pair_key <- paste(
  cpg_gene_regulatory_annotation$probe_id,
  cpg_gene_regulatory_annotation$gene_id_base,
  sep = "|"
)

if (anyDuplicated(pair_key) > 0) {
  stop("CpG-gene regulatory annotation contains duplicated pairs.")
}

cpg_gene_counts <- aggregate(
  gene_id_base ~ probe_id,
  data = cpg_gene_regulatory_annotation,
  FUN = function(values) {
    length(unique(values))
  }
)

names(cpg_gene_counts)[2] <- "n_protein_coding_genes"

promoter_gene_counts <- aggregate(
  gene_id_base ~ probe_id,
  data = cpg_gene_regulatory_annotation[
    cpg_gene_regulatory_annotation$promoter_associated,
  ],
  FUN = function(values) {
    length(unique(values))
  }
)

names(promoter_gene_counts)[2] <- "n_promoter_genes"

transcript_gene_counts <- aggregate(
  gene_id_base ~ probe_id,
  data = cpg_gene_regulatory_annotation[
    cpg_gene_regulatory_annotation$transcript_associated,
  ],
  FUN = function(values) {
    length(unique(values))
  }
)

names(transcript_gene_counts)[2] <- "n_transcript_genes"

cpg_annotation_coverage <- merge(
  hm450_cpg_lookup,
  cpg_gene_counts,
  by = "probe_id",
  all.x = TRUE,
  sort = FALSE
)

cpg_annotation_coverage <- merge(
  cpg_annotation_coverage,
  promoter_gene_counts,
  by = "probe_id",
  all.x = TRUE,
  sort = FALSE
)

cpg_annotation_coverage <- merge(
  cpg_annotation_coverage,
  transcript_gene_counts,
  by = "probe_id",
  all.x = TRUE,
  sort = FALSE
)

count_columns <- c(
  "n_protein_coding_genes",
  "n_promoter_genes",
  "n_transcript_genes"
)

for (column in count_columns) {
  cpg_annotation_coverage[[column]][
    is.na(cpg_annotation_coverage[[column]])
  ] <- 0L
  
  cpg_annotation_coverage[[column]] <- as.integer(
    cpg_annotation_coverage[[column]]
  )
}

cpg_annotation_coverage$promoter_associated <- (
  cpg_annotation_coverage$n_promoter_genes > 0L
)

cpg_annotation_coverage$transcript_associated <- (
  cpg_annotation_coverage$n_transcript_genes > 0L
)

cpg_annotation_coverage$annotation_status <- ifelse(
  cpg_annotation_coverage$promoter_associated &
    cpg_annotation_coverage$transcript_associated,
  "promoter_and_transcript",
  ifelse(
    cpg_annotation_coverage$promoter_associated,
    "promoter_only",
    ifelse(
      cpg_annotation_coverage$transcript_associated,
      "transcript_only",
      "no_protein_coding_gene_mapping"
    )
  )
)

cpg_annotation_coverage <- cpg_annotation_coverage[
  order(cpg_annotation_coverage$probe_id),
]

row.names(cpg_annotation_coverage) <- NULL

if (nrow(cpg_annotation_coverage) != length(hm450_cpg_manifest)) {
  stop("CpG-level annotation coverage does not preserve the full CpG manifest.")
}

if (anyDuplicated(cpg_annotation_coverage$probe_id) > 0) {
  stop("CpG-level annotation coverage contains duplicated probe IDs.")
}

if (
  sum(cpg_annotation_coverage$n_protein_coding_genes) !=
  nrow(cpg_gene_regulatory_annotation)
) {
  stop("CpG-gene pair counts are inconsistent with CpG-level coverage.")
}

if (
  sum(cpg_annotation_coverage$n_promoter_genes) !=
  nrow(promoter_cpg_gene_pairs)
) {
  stop("Promoter-pair counts are inconsistent with CpG-level coverage.")
}

if (
  sum(cpg_annotation_coverage$n_transcript_genes) !=
  nrow(genic_cpg_gene_pairs)
) {
  stop("Transcript-pair counts are inconsistent with CpG-level coverage.")
}

cat(
  "HM450 CpGs represented:",
  nrow(cpg_annotation_coverage),
  "\n"
)

cat(
  "CpGs with >=1 protein-coding gene mapping:",
  sum(cpg_annotation_coverage$n_protein_coding_genes > 0L),
  "\n"
)

cat(
  "CpGs without protein-coding gene mapping:",
  sum(cpg_annotation_coverage$n_protein_coding_genes == 0L),
  "\n"
)

cat(
  "Total unique CpG-gene pairs:",
  sum(cpg_annotation_coverage$n_protein_coding_genes),
  "\n\n"
)

print(
  table(cpg_annotation_coverage$annotation_status)
)





# =============================================================================
# Define annotation output paths
# =============================================================================

annotation_output_dir <- file.path(
  repo_root,
  "data",
  "raw",
  "tcga",
  "annotations",
  "sesame_hm450_hg38"
)

cpg_coverage_path <- file.path(
  annotation_output_dir,
  "sesame_hm450_hg38_cpg_annotation_coverage.csv"
)

cpg_gene_annotation_path <- file.path(
  annotation_output_dir,
  "sesame_hm450_hg38_cpg_gene_regulatory_annotation.csv"
)

annotation_metadata_path <- file.path(
  annotation_output_dir,
  "sesame_hm450_hg38_annotation_metadata.csv"
)





# =============================================================================
# Finalize and export frozen HM450 hg38 annotation artifacts
# =============================================================================

collapse_transcript_ids <- function(values) {
  paste(
    sort(unique(values)),
    collapse = ";"
  )
}

promoter_transcript_ids <- aggregate(
  transcript_id ~ probe_id + gene_id_base,
  data = promoter_annotation,
  FUN = collapse_transcript_ids
)

names(promoter_transcript_ids)[3] <- "promoter_transcript_ids"

genic_transcript_ids <- aggregate(
  transcript_id ~ probe_id + gene_id_base,
  data = genic_annotation,
  FUN = collapse_transcript_ids
)

names(genic_transcript_ids)[3] <- "genic_transcript_ids"

cpg_gene_regulatory_annotation <- merge(
  cpg_gene_regulatory_annotation,
  promoter_transcript_ids,
  by = c("probe_id", "gene_id_base"),
  all.x = TRUE,
  sort = FALSE
)

cpg_gene_regulatory_annotation <- merge(
  cpg_gene_regulatory_annotation,
  genic_transcript_ids,
  by = c("probe_id", "gene_id_base"),
  all.x = TRUE,
  sort = FALSE
)

cpg_gene_regulatory_annotation$promoter_transcript_ids[
  is.na(cpg_gene_regulatory_annotation$promoter_transcript_ids)
] <- ""

cpg_gene_regulatory_annotation$genic_transcript_ids[
  is.na(cpg_gene_regulatory_annotation$genic_transcript_ids)
] <- ""

cpg_gene_regulatory_annotation <- cpg_gene_regulatory_annotation[
  order(
    cpg_gene_regulatory_annotation$probe_id,
    cpg_gene_regulatory_annotation$gene_id_base
  ),
]

row.names(cpg_gene_regulatory_annotation) <- NULL

if (anyDuplicated(
  paste(
    cpg_gene_regulatory_annotation$probe_id,
    cpg_gene_regulatory_annotation$gene_id_base,
    sep = "|"
  )
) > 0) {
  stop("Final CpG-gene annotation contains duplicated inferential pairs.")
}

if (
  nrow(cpg_gene_regulatory_annotation) != 441122L
) {
  stop("Unexpected number of final CpG-gene regulatory pairs.")
}

if (
  nrow(cpg_annotation_coverage) != 482389L
) {
  stop("Unexpected number of CpG-level annotation rows.")
}

annotation_metadata <- data.frame(
  field = c(
    "annotation_freeze_date",
    "retrieval_date",
    "source_database",
    "provider",
    "retrieval_method",
    "bioconductor_release",
    "r_version",
    "sesameData_version",
    "platform",
    "genome_build",
    "manifest_resource",
    "manifest_resource_ehid",
    "manifest_resource_version",
    "manifest_source_version",
    "genome_resource",
    "genome_resource_ehid",
    "genome_resource_version",
    "genome_source_version",
    "gene_annotation_scope",
    "manifest_function",
    "transcript_function",
    "promoter_method",
    "promoter_upstream_bp",
    "promoter_downstream_bp",
    "overlap_function",
    "overlap_strand_policy",
    "cpg_identifier_rule",
    "multi_gene_mapping_policy",
    "transcript_collapse_policy",
    "unmapped_cpg_policy",
    "derivation_script",
    "hm450_manifest_loci",
    "hm450_cpg_probes",
    "protein_coding_genes",
    "cpgs_with_protein_coding_mapping",
    "cpgs_without_protein_coding_mapping",
    "unique_cpg_gene_pairs"
  ),
  value = c(
    "2026-09-08",
    "2026-09-08",
    "Bioconductor",
    "SeSAMe / sesameData",
    "sesameData / ExperimentHub cached resource retrieval",
    "3.23",
    "4.6.1",
    "1.30.0",
    "HM450",
    "hg38",
    "HM450.address",
    "EH7317",
    "1.13.1",
    "2022-01-23",
    "genomeInfo.hg38",
    "EH8558",
    "1.21.1",
    "2024-01-11",
    "protein_coding",
    "sesameData_getManifestGRanges",
    "sesameData_getTxnGRanges",
    "GenomicRanges::promoters",
    as.character(PROMOTER_UPSTREAM_BP),
    as.character(PROMOTER_DOWNSTREAM_BP),
    "GenomicRanges::findOverlaps",
    "ignore.strand=TRUE",
    "^cg[0-9]{8}$",
    "retain_all_valid_protein_coding_cpg_gene_pairs",
    "collapse_exact_cpg_gene_pairs_preserve_sorted_transcript_ids",
    "retain_in_cpg_coverage_as_no_protein_coding_gene_mapping",
    script_relative_path,
    as.character(length(hm450_hg38_manifest)),
    as.character(length(hm450_cpg_manifest)),
    as.character(length(unique(protein_coding_gene_ids_base))),
    as.character(sum(cpg_annotation_coverage$n_protein_coding_genes > 0L)),
    as.character(sum(cpg_annotation_coverage$n_protein_coding_genes == 0L)),
    as.character(nrow(cpg_gene_regulatory_annotation))
  ),
  stringsAsFactors = FALSE
)

dir.create(
  annotation_output_dir,
  recursive = TRUE,
  showWarnings = FALSE
)

write.table(
  cpg_annotation_coverage,
  file = cpg_coverage_path,
  sep = ",",
  row.names = FALSE,
  col.names = TRUE,
  quote = TRUE,
  na = "",
  eol = "\n",
  fileEncoding = "UTF-8"
)

write.table(
  cpg_gene_regulatory_annotation,
  file = cpg_gene_annotation_path,
  sep = ",",
  row.names = FALSE,
  col.names = TRUE,
  quote = TRUE,
  na = "",
  eol = "\n",
  fileEncoding = "UTF-8"
)

write.table(
  annotation_metadata,
  file = annotation_metadata_path,
  sep = ",",
  row.names = FALSE,
  col.names = TRUE,
  quote = TRUE,
  na = "",
  eol = "\n",
  fileEncoding = "UTF-8"
)

output_paths <- c(
  cpg_coverage_path,
  cpg_gene_annotation_path,
  annotation_metadata_path
)

if (!all(file.exists(output_paths))) {
  stop("One or more annotation artifacts were not written successfully.")
}

cat(
  "Export complete.\n",
  "CpG coverage rows:",
  nrow(cpg_annotation_coverage),
  "\n",
  "CpG-gene rows:",
  nrow(cpg_gene_regulatory_annotation),
  "\n",
  "Metadata rows:",
  nrow(annotation_metadata),
  "\n\n"
)

print(
  data.frame(
    file = basename(output_paths),
    size_bytes = file.info(output_paths)$size,
    stringsAsFactors = FALSE
  )
)





