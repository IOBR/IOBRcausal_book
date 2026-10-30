<!-- Generated from methods/index.qmd. Edit the QMD source and rebuild. -->

# Choose a method

[Book contents](../../README.md) · [Previous: Diagnostics and sensitivity](../results/diagnostics.md) · [Next: GLM (Generalized Linear Model)](glm.md)

Start with the study question, exposure contrast, outcome and adjustment set.
Method availability depends on that combination. The original eight estimator
families are retained here, with examples aligned to the current public wrappers.

| Method | Main use | Read next |
| --- | --- | --- |
| GLM | Adjusted outcome regression | [GLM](glm.md) |
| G-Computation | Average modeled outcomes under exposure contrasts | [G-Computation](gcomp.md) |
| AIPW | Outcome and propensity models with optional cross-fitting | [AIPW](aipw.md) |
| IPW | Propensity-based weighting | [IPW](ipw.md) |
| TMLE | Targeted outcome-model updating | [TMLE](tmle.md) |
| PSM | Propensity-score matching | [PSM](psm.md) |
| Causal Forest | Exploratory effect heterogeneity | [Causal Forest](causal-forest.md) |
| GPS | Dose contrasts for a continuous exposure | [GPS](gps.md) |

[Multi-method comparison](comparison.md) is a comparison utility, not a ninth
estimator or a vote on causality. Compare only compatible targets and scales.

## Synthetic example data

[Download methods-data.R](../../assets/downloads/methods-data.R), save it in your
working directory, and run:

```r
library(IOBRcausal)
source("methods-data.R")
str(data)
```

The script creates 240 fictional subjects and defines `data`, including the
columns used on the method pages. `Immunotherapy` is a simulated binary exposure;
`TMB` is a simulated continuous exposure. The response, continuous outcome and
survival times are also artificial. Use the examples to learn the interface,
not to make clinical claims or calibrate a method.

## Read the returned contract

Check `Scale`, contrast, uncertainty, method status, support and diagnostics.
Binary, continuous and survival refer to outcome types; the exposure has its own
type. Continuous-exposure policies and survival horizons can require the core
`iobr_causal_estimate()` interface rather than a convenience wrapper.

Use the [support reference](../reference/validation.md) for implementation and
validation limits. For complete analysis delivery through one request, return
to the [workflow chapters](../workflows/pathway-first.md).

---

[Book contents](../../README.md) · [Previous: Diagnostics and sensitivity](../results/diagnostics.md) · [Next: GLM (Generalized Linear Model)](glm.md)
