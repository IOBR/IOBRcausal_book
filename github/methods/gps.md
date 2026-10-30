<!-- Generated from methods/gps.qmd. Edit the QMD source and rebuild. -->

# GPS (Generalized Propensity Score - Continuous Exposure)

[Book contents](../../README.md) · [Previous: Causal Forest](causal-forest.md) · [Next: Multi-Method Comparison](comparison.md)

Use the [synthetic data setup](index.md#synthetic-example-data) first; it defines
`data` and the columns used below. These are advanced direct R examples.

Compare specified doses of a continuous exposure, even when the outcome is binary.
Keep the exposure contrast explicit when reporting a risk or mean difference.

## Continuous outcome

```r
gps_continuous <- causal_gps(
  data = data, treatment = "TMB", outcome = "TumorChange",
  confounders = c("Age", "Sex", "ECOG"),
  outcome_type = "continuous", boot_R = 300
)
```

This returns a mean difference for the specified dose contrast.

## Binary outcome

```r
gps_result <- causal_gps(
  data = data,
  treatment = "TMB",  # Continuous exposure variable
  outcome = "Response",
  confounders = c("Age", "Sex", "ECOG"),
  outcome_type = "binary",
  boot_R = 300
)
# Output: Risk Difference
```

Small binary-outcome bootstrap fits can warn that fitted probabilities are
numerically 0 or 1; this occurs in the supplied synthetic example. Inspect the
fit and support diagnostics. A finite returned estimate does not resolve those
warnings or establish calibrated uncertainty.

## Read the result

GPS requires a continuous exposure. The binary-outcome example compares the default specified dose contrast on the RiskDiff scale; it is not an OR or a per-unit regression coefficient. Survival GPS is not implemented. Inspect dose support and the returned contrast.

See [effect scales and reporting](../results/reading-results.md),
[diagnostics](../results/diagnostics.md) and the
[current support reference](../reference/validation.md).

---

[Book contents](../../README.md) · [Previous: Causal Forest](causal-forest.md) · [Next: Multi-Method Comparison](comparison.md)
