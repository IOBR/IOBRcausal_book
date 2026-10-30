<!-- Generated from methods/ipw.qmd. Edit the QMD source and rebuild. -->

# IPW (Inverse Probability Weighting)

[Book contents](../../README.md) · [Previous: AIPW (Augmented Inverse Probability Weighting)](aipw.md) · [Next: TMLE (Targeted Maximum Likelihood Estimation)](tmle.md)

Use the [synthetic data setup](index.md#synthetic-example-data) first; it defines
`data` and the columns used below. These are advanced direct R examples.

Use propensity-based weights to adjust for measured confounders. Inspect overlap,
weight extremes and effective sample size before interpreting the estimates.

```r
ipw_result <- causal_ipw(data, "Immunotherapy", "Response",
                        confounders = c("Age", "Sex", "Stage", "ECOG"),
                        outcome_type = "binary",
                        stabilize = TRUE)  # Use stabilized weights
```

## Read the result

The wrapper parameter is `stabilize`. Inspect positivity, raw and truncated weights and effective sample size. A binary-exposure survival HR is a limited weighted Cox summary; continuous-exposure primary survival estimation is not implemented for this method.

See [effect scales and reporting](../results/reading-results.md),
[diagnostics](../results/diagnostics.md) and the
[current support reference](../reference/validation.md).

---

[Book contents](../../README.md) · [Previous: AIPW (Augmented Inverse Probability Weighting)](aipw.md) · [Next: TMLE (Targeted Maximum Likelihood Estimation)](tmle.md)
