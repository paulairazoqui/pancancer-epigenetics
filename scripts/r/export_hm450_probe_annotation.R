# =======================================================
# Export HM450 probe annotation from Bioconductor
# =======================================================

# Detect the repository root
project_root <- normalizePath(
  getwd(),
  winslash = "/",
  mustWork = TRUE
)

while (!file.exists(file.path(project_root, "pyproject.toml"))) {
  parent_directory <- dirname(project_root)
  
  if (identical(parent_directory, project_root)) {
    stop(
      "Could not locate the pancancer-epigenetics repository root."
    )
  }
  
  project_root <- parent_directory
}

setwd(project_root)


# =======================================================
# Load annotation packages
# =======================================================

suppressPackageStartupMessages({
  library(minfi)
  library(
    IlluminaHumanMethylation450kanno.ilmn12.hg19
  )
})


# =======================================================
# Build HM450 probe-annotation table
# =======================================================

hm450_probe_annotation <- as.data.frame(
  getAnnotation(
    IlluminaHumanMethylation450kanno.ilmn12.hg19
  ),
  stringsAsFactors = FALSE
)

hm450_probe_annotation <- data.frame(
  probe_id = rownames(hm450_probe_annotation),
  hm450_probe_annotation,
  row.names = NULL,
  check.names = FALSE
)


# =======================================================
# Export HM450 probe annotation
# =======================================================

hm450_annotation_path <- file.path(
  "data",
  "interim",
  "metadata",
  "illumina_hm450_ilmn12_hg19_probe_annotation.csv"
)

dir.create(
  dirname(hm450_annotation_path),
  recursive = TRUE,
  showWarnings = FALSE
)

write.csv(
  hm450_probe_annotation,
  hm450_annotation_path,
  row.names = FALSE,
  na = ""
)


# =======================================================
# Report exported artifact and software versions
# =======================================================

cat("HM450 probe annotation exported.\n")
cat("Path:", hm450_annotation_path, "\n")
cat(
  "Shape:",
  nrow(hm450_probe_annotation),
  "x",
  ncol(hm450_probe_annotation),
  "\n"
)
cat(
  "Unique probe IDs:",
  length(unique(hm450_probe_annotation$probe_id)),
  "\n"
)
cat(
  "R version:",
  R.version.string,
  "\n"
)
cat(
  "minfi version:",
  as.character(packageVersion("minfi")),
  "\n"
)
cat(
  "Annotation package version:",
  as.character(
    packageVersion(
      "IlluminaHumanMethylation450kanno.ilmn12.hg19"
    )
  ),
  "\n"
)