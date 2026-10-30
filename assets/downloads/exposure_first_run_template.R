# Agent specified-feature template: one public request/complete-workflow entry.
# Replace the syntax examples with the inspected, agreed clinical specification.
# Sourcing defines main() only. Rscript plans by default; --run executes.
# An already authorized analysis may call main(plan_only = FALSE) directly.

main <- function(plan_only = TRUE, project = getwd()) {
  library(IOBRcausal)
  data_path <- file.path(project, "02-input", "analysis_table.csv")
  output_root <- file.path(project, "04-report", "exposure_first")
  dat <- utils::read.csv(data_path, stringsAsFactors = FALSE, check.names = FALSE)

  # Include exactly the requested features; other numeric columns stay out.
  features <- c("T_cell_inflamed_score", "Myeloid_score")
  covariates <- c("Age", "Sex", "ECOG")
  # Response only: endpoints <- list(binary = "Response")
  # Add binary = "Response" only when both endpoints were requested.
  endpoints <- list(time = "OS_time", status = "OS_status", event = 1,
                    time_unit = "months")
  request <- list(operation = "analyze", workflow = "exposure_first",
    analysis_type = "association", features = features, covariates = covariates,
    endpoints = endpoints, methods = "GLM", parameters = list(
      complete_workflow = TRUE, seed = 20261029L, profile = "standard"))
  # Keep agreed supported thresholds/bootstrap settings in this request. Do not
  # chain a second candidate workflow or lower repetitions after a failure.

  run <- iobrcausal(request = request, inputs = list(data = dat),
    output_dir = output_root, plan_only = plan_only, project = project)
  print(run)
  if (!isTRUE(plan_only) && !is.null(run$workflow$delivery_dir))
    message("Read first: ", file.path(run$workflow$delivery_dir, "README.md"))
  invisible(run)
}

if (sys.nframe() == 0L) main(plan_only = !"--run" %in% commandArgs(trailingOnly = TRUE))
