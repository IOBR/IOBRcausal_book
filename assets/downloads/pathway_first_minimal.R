# Synthetic pathway-first example through the common Agent execution entry.
# Rscript pathway_first_minimal.R previews; add --run for the authorized demo.
# No API/provider is required. Do not chain a lower-level workflow afterwards.
library(IOBRcausal)

set.seed(20260806)
n <- 80L
sample_id <- sprintf("S%03d", seq_len(n))
response <- rep(c(0L, 1L), each = n / 2L)
gene_sets <- iobr_causal_iobr_gene_sets(signatures = c("CD_8_T_effector", "APM"))
genes <- unique(unlist(gene_sets, use.names = FALSE))
expression <- matrix(stats::rnorm(length(genes) * n, sd = .70), nrow = length(genes),
  dimnames = list(genes, sample_id))
expression[gene_sets$CD_8_T_effector, response == 1L] <-
  expression[gene_sets$CD_8_T_effector, response == 1L] + .40
clinical <- data.frame(Sample_ID = sample_id, Response = response)
output_root <- Sys.getenv("IOBRCAUSAL_EXAMPLE_OUTPUT",
  unset = file.path("iobrcausal_runs", "pathway_first_minimal"))
request <- list(operation = "analyze", workflow = "pathway_first",
  analysis_type = "association", covariates = character(),
  endpoints = list(binary = "Response"), methods = "GLM",
  parameters = list(complete_workflow = TRUE, seed = 20260806L,
    genes_in = "rows", sample_id_col = "Sample_ID", min_genes_per_pathway = 2L,
    formats = "png"))
result <- iobrcausal(request = request,
  inputs = list(expression = expression, clinical = clinical, gene_sets = gene_sets),
  output_dir = output_root, plan_only = !"--run" %in% commandArgs(trailingOnly = TRUE))
print(result)
if (!is.null(result$workflow$delivery_dir) && dir.exists(result$workflow$delivery_dir))
  message("Read first: ", file.path(result$workflow$delivery_dir, "README.md"))
