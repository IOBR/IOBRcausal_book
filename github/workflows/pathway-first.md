<!-- Generated from workflows/pathway-first.qmd. Edit the QMD source and rebuild. -->

# From expression to pathways and genes

[Book contents](../../README.md) · [Previous: Prepare your data](../data-preparation.md) · [Next: Analyse a specified gene or score](exposure-first.md)

Use this route when you have expression and clinical data and want to discover
pathways before following their member genes. Prepare the inputs as described in
[data preparation](../data-preparation.md).

## Read your files

For this CSV layout, the first expression column contains gene IDs and the
remaining columns contain numeric expression values, one sample per column.
The clinical table has a `Sample_ID` column matching those sample names.
Replace the file paths with your own:

```r
library(IOBRcausal)
expression <- as.matrix(read.csv(
  "expression.csv", row.names = 1, check.names = FALSE
))
clinical <- read.csv("clinical.csv", stringsAsFactors = FALSE, check.names = FALSE)
gene_sets <- iobr_causal_iobr_gene_sets(
  signatures = c("CD_8_T_effector", "APM")
)
```

The clinical file must also contain the Response and covariate columns used
below. Check their definitions against your codebook before execution.

## Run one complete workflow

This example requests ordinary Response association only:

```r
request <- list(
  operation = "analyze", workflow = "pathway_first",
  analysis_type = "association", covariates = c("Age", "Sex", "ECOG"),
  endpoints = list(binary = "Response"), methods = "GLM",
  parameters = list(
    complete_workflow = TRUE, seed = 20261030L,
    genes_in = "rows", sample_id_col = "Sample_ID", profile = "standard"
  )
)
run <- iobrcausal(
  request = request,
  inputs = list(expression = expression, clinical = clinical, gene_sets = gene_sets),
  output_dir = "results/pathway_first", plan_only = TRUE
)
```

Inspect the plan and resolve material input problems. To execute the same
request, call it with `plan_only = FALSE`. Keep the agreed endpoint, covariates,
seed and evidence rules. The [downloadable example](../../assets/downloads/pathway_first_minimal.R)
provides complete synthetic inputs and an explicit `--run` option.

## Choose gene sets

The input example selects two bundled signatures. For your own sets, supply a named list of
gene members. Record the source, version, identifier namespace and matched
coverage. Supported on-demand curated collections also need source provenance;
their availability does not make every score biologically validated.

## Follow the stages

The route checks data, scores pathways, screens requested endpoints, estimates
eligible pathways, maps original members and follows genes. It then collects
diagnostics, validates outputs and writes reports and saved-number figures.
Use `run$workflow$stages` to inspect the actual status of each step.

The output keeps full pathway-gene mappings. A representative pathway is a
display assignment; it does not replace the full mapping or allow a gene to
inherit a pathway's P value or FDR.

For an OS-only request, use `endpoints = list(time = "OS_time", status = "OS_status",
event = 1, time_unit = "months")`. Add a binary endpoint only if both were
requested. Response and OS retain separate estimates and testing families.

Open the delivery README, then the endpoint workbook and its diagnostics.
Continue with [reading results](../results/reading-results.md).

---

[Book contents](../../README.md) · [Previous: Prepare your data](../data-preparation.md) · [Next: Analyse a specified gene or score](exposure-first.md)
