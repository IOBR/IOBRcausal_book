<!-- Generated from reference/validation.qmd. Edit the QMD source and rebuild. -->

# Validation and method support

[Book contents](../../README.md) · [Previous: Troubleshooting](troubleshooting.md) · [Next: Advanced analysis](advanced.md)

This Book documents package **32.2.3**. The release decision remains
**NOT_RELEASE_READY**. A readable Book, a successful installation and a passed
synthetic example are separate from statistical calibration or release validation.

## Runtime support

The executable method matrix depends on exposure type, outcome, analysis mode
and target estimand. A stable runtime label means an implemented path in eligible
settings; it does not certify all assumptions or validate every combination.

[Download the complete support snapshot](../../assets/downloads/method-support-32.2.3.csv).
It preserves support, assumptions, skip reasons and historical evidence fields.
The snapshot was generated on 2026-10-29 without fitting an estimator. Its
documentation date is not a new benchmark date.

| Method family | Important limit |
| --- | --- |
| GLM | Regression summaries and survival targets need their own scales and assumptions |
| GComp | Eligible survival contrasts are RMST or survival-probability differences |
| AIPW / TMLE | Risk/mean differences; policy and survival paths have separate limits |
| IPW / PSM | Binary-exposure survival HR is limited; primary continuous-exposure survival is unsupported |
| Causal Forest | Exploratory heterogeneity; no individually calibrated treatment rule |
| GPS | Continuous exposure only; survival GPS is not implemented |

Convenience wrappers do not expose every advanced setting. Some dedicated
adapters, including longitudinal and frozen OS mediation paths, are outside the
formal matrix and have separate contracts.

## What documentation checks establish

Book checks cover rendering, local links and anchors, resource integrity,
English content, migration coverage and selected synthetic examples. They do
not update the row-wise Codex acceptance fields in the method snapshot, rerun
patient analyses or establish a biological mechanism.

For any scientific result, retain its exact code version, inputs, requested
family, effective settings, complete numeric output and diagnostic findings.
Historical evidence stays labeled with its original scope and version.

---

[Book contents](../../README.md) · [Previous: Troubleshooting](troubleshooting.md) · [Next: Advanced analysis](advanced.md)
