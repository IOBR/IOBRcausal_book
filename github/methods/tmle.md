<!-- Generated from methods/tmle.qmd. Edit the QMD source and rebuild. -->

# TMLE (Targeted Maximum Likelihood Estimation)

[Book contents](../../README.md) · [Previous: IPW (Inverse Probability Weighting)](ipw.md) · [Next: PSM (Propensity Score Matching)](psm.md)

Use the [synthetic data setup](index.md#synthetic-example-data) first; it defines
`data` and the columns used below. These are advanced direct R examples.

Target outcome-model estimates using propensity information. Binary-outcome
contrasts are reported on the risk-difference scale.

```r
tmle_result <- causal_tmle(data, "Immunotherapy", "Response",
                           confounders = c("Age", "Sex", "Stage", "ECOG"),
                           outcome_type = "binary")
```

## Read the result

Optional TMLE dependencies must be installed for eligible calls. Non-survival outputs are RiskDiff or MeanDiff. Survival and continuous-policy branches have separate support limits; a runtime support label is not a current validation result.

See [effect scales and reporting](../results/reading-results.md),
[diagnostics](../results/diagnostics.md) and the
[current support reference](../reference/validation.md).

---

[Book contents](../../README.md) · [Previous: IPW (Inverse Probability Weighting)](ipw.md) · [Next: PSM (Propensity Score Matching)](psm.md)
