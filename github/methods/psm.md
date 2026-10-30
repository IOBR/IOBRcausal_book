<!-- Generated from methods/psm.qmd. Edit the QMD source and rebuild. -->

# PSM (Propensity Score Matching)

[Book contents](../../README.md) · [Previous: TMLE (Targeted Maximum Likelihood Estimation)](tmle.md) · [Next: Causal Forest](causal-forest.md)

Use the [synthetic data setup](index.md#synthetic-example-data) first; it defines
`data` and the columns used below. These are advanced direct R examples.

Match observations on propensity scores, then inspect balance and overlap in the
matched sample.

```r
psm_result <- causal_psm(data, "Immunotherapy", "Response",
                        confounders = c("Age", "Sex", "Stage", "ECOG"),
                        outcome_type = "binary",
                        match_method = "nearest",  # "nearest", "optimal", "full"
                        caliper = 0.2,
                        ratio = 1)  # 1:1 matching
```

## Read the result

Check the matched population, caliper, ratio, overlap and balance. Matching changes the comparison sample and does not control unmeasured confounding. A binary-exposure survival HR is a limited matched Cox summary; continuous-exposure primary survival estimation is not implemented.

See [effect scales and reporting](../results/reading-results.md),
[diagnostics](../results/diagnostics.md) and the
[current support reference](../reference/validation.md).

---

[Book contents](../../README.md) · [Previous: TMLE (Targeted Maximum Likelihood Estimation)](tmle.md) · [Next: Causal Forest](causal-forest.md)
