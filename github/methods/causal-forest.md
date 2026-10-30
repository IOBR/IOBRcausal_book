<!-- Generated from methods/causal-forest.qmd. Edit the QMD source and rebuild. -->

# Causal Forest

[Book contents](../../README.md) · [Previous: PSM (Propensity Score Matching)](psm.md) · [Next: GPS (Generalized Propensity Score - Continuous Exposure)](gps.md)

Use the [synthetic data setup](index.md#synthetic-example-data) first; it defines
`data` and the columns used below. These are advanced direct R examples.

Explore how estimated effects vary across covariate profiles. The returned CATE
scores are exploratory heterogeneity rankings, not individually calibrated effects
or validated treatment-selection rules.

```r
cf_result <- causal_forest_estimate(
  data,
  treatment = "Immunotherapy",
  outcome = "Response",
  confounders = c("Age", "Sex", "Stage", "ECOG"),
  outcome_type = "binary",
  num_trees = 2000
)

# Extract exploratory heterogeneity scores (CATE)
hte <- get_hte(cf_result)
if (!is.null(hte)) {
  cate_mean <- mean(hte$CATE$CATE)
  print(paste("Mean exploratory CATE score:", round(cate_mean, 3)))
  print(hte$Variable_Importance)
}
```

## Read the result

Install the optional `grf` dependency to run this example. The `num_trees` wrapper setting reaches the core forest. Binary exposures produce exploratory ATE/CATE differences; continuous exposures use average partial effects. Survival forests target RMST or survival-probability differences, not HR.

See [effect scales and reporting](../results/reading-results.md),
[diagnostics](../results/diagnostics.md) and the
[current support reference](../reference/validation.md).

---

[Book contents](../../README.md) · [Previous: PSM (Propensity Score Matching)](psm.md) · [Next: GPS (Generalized Propensity Score - Continuous Exposure)](gps.md)
