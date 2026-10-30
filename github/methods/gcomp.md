<!-- Generated from methods/gcomp.qmd. Edit the QMD source and rebuild. -->

# G-Computation

[Book contents](../../README.md) · [Previous: GLM (Generalized Linear Model)](glm.md) · [Next: AIPW (Augmented Inverse Probability Weighting)](aipw.md)

Use the [synthetic data setup](index.md#synthetic-example-data) first; it defines
`data` and the columns used below. These are advanced direct R examples.

Average model-predicted outcomes under specified exposure contrasts.

```r
gcomp_result <- causal_gcomp(data, "Immunotherapy", "Response",
                             confounders = c("Age", "Sex", "Stage", "ECOG"),
                             outcome_type = "binary",
                             boot_R = 500)
```

## Read the result

Binary-outcome contrasts can include RiskDiff, RiskRatio and MarginalOR. Keep the requested exposure contrast and bootstrap settings. Eligible survival paths target RMST or survival-probability differences, not a hazard ratio.

See [effect scales and reporting](../results/reading-results.md),
[diagnostics](../results/diagnostics.md) and the
[current support reference](../reference/validation.md).

---

[Book contents](../../README.md) · [Previous: GLM (Generalized Linear Model)](glm.md) · [Next: AIPW (Augmented Inverse Probability Weighting)](aipw.md)
