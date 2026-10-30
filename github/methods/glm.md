<!-- Generated from methods/glm.qmd. Edit the QMD source and rebuild. -->

# GLM (Generalized Linear Model)

[Book contents](../../README.md) · [Previous: Choose a method](index.md) · [Next: G-Computation](gcomp.md)

Use the [synthetic data setup](index.md#synthetic-example-data) first; it defines
`data` and the columns used below. These are advanced direct R examples.

Fit adjusted logistic, linear or survival regression models as a baseline analysis.
Survival estimation defaults to an RMST difference. The Cox examples explicitly
request `hazard_ratio`; read `Scale` to distinguish HR from Log-HR.

```r
# Binary outcome (logistic regression; check Scale for OR or Log-OR)
glm_bin <- causal_glm(data, "Immunotherapy", "Response",
                     confounders = c("Age", "Sex", "Stage", "ECOG"),
                     outcome_type = "binary")

# Continuous outcome (Linear regression, outputs coefficient)
glm_cont <- causal_glm(data, "Immunotherapy", "TumorChange",
                      confounders = c("Age", "Sex", "Stage", "ECOG"),
                      outcome_type = "continuous")

# Survival outcome (Cox summary; check Scale for HR or Log-HR)
glm_surv <- causal_glm(data, "Immunotherapy", "OS_months",
                      confounders = c("Age", "Sex", "Stage", "ECOG"),
                      outcome_type = "survival",
                      os_time = "OS_months",
                      os_status = "OS_event",
                      estimand = "hazard_ratio")
```

## Read the result

For continuous exposures, logistic output may be Log-OR. For a Cox summary, request `estimand = "hazard_ratio"` explicitly and check HR versus Log-HR. Default survival estimation targets an RMST difference; supported fixed-horizon probability contrasts are distinct targets.

See [effect scales and reporting](../results/reading-results.md),
[diagnostics](../results/diagnostics.md) and the
[current support reference](../reference/validation.md).

---

[Book contents](../../README.md) · [Previous: Choose a method](index.md) · [Next: G-Computation](gcomp.md)
