<!-- Generated from results/reading-results.qmd. Edit the QMD source and rebuild. -->

# Read the results

[Book contents](../../README.md) · [Previous: Read or plot saved results](../workflows/saved-results.md) · [Next: Diagnostics and sensitivity](diagnostics.md)

Start with the README in the returned delivery directory. It links the actual
reports and states what completed. Then open the requested endpoint workbook.

## Choose the workbook

| File | Use |
| --- | --- |
| `01_ORR_pathway_first_report.xlsx` | Response pathway and gene results |
| `02_Survival_pathway_first_report.xlsx` | Survival pathway and gene results |
| `03_Integrated_review_report.xlsx` | Cross-endpoint pathway/gene review |
| `01_ORR_exposure_first_report.xlsx` | Response results for named features |
| `02_Survival_exposure_first_report.xlsx` | Survival results for named features |
| `03_Exposure_integrated_review_report.xlsx` | Cross-endpoint exposure review |

Only requested, available endpoints should supply results. An absent endpoint
or empty placeholder is not a reason to add an unrequested analysis. If Excel
writers are unavailable, inspect the reported CSV fallback.

## Read these sheets first

1. `00_READ_FIRST` and `02_Parameter_Settings`: scope, thresholds and settings.
2. Endpoint statistics and method details: actual numbers, method and scale.
3. Diagnostics, sensitivity and skipped/failed rows: limitations and exclusions.
4. `Column_Dictionary` and the method/claim guides: interpretation of each field.
5. Integrated review: compare endpoints after reading their separate results.

Pathway-first gene reports use `Gene_Stats`, `Gene_Method_Details`,
`Gene_Explain` and `Gene_Full_Audit`. Exposure-first uses the corresponding
`Exposure_*` sheets. Keep the full audit tables when sharing a compact display.

## Read the effect scale

| Scale | Null | Meaning |
| --- | --- | --- |
| OR / RR | 1 | Relative odds / risk for the stated contrast |
| Log-OR | 0 | Log odds ratio; exponentiate estimate and CI together for OR |
| HR | 1 | Relative event hazard under the stated Cox summary |
| Log-HR | 0 | Log hazard ratio; exponentiate estimate and CI together for HR |
| RiskDiff | 0 | Absolute difference in outcome probability |
| MeanDiff | 0 | Difference in the original outcome units |
| RMST_Diff | 0 | Difference in restricted mean survival up to the specified horizon |
| SurvDiff | 0 | Difference in survival probability at the specified horizon |

Read the contrast too: per unit, per SD, two doses and intervention policies
answer different questions. HR is not a probability ratio or an absolute gain
in survival. Screening ORs and formal risk differences are different results.

## Report a result

Give the cohort, endpoint coding, contrast, covariates, method, scale, estimate,
CI and actual P/FDR family. Add the support level and the main diagnostic finding.
Association, screening, statistical mediation and functional mechanism evidence
are distinct claims. Method agreement or a small P value does not prove causality.

FDR is adjusted over the requested family, not just rows selected for display.
Retain failed or unestimable rows in the scope accounting. Continue with
[diagnostics](diagnostics.md) before choosing headline results.

---

[Book contents](../../README.md) · [Previous: Read or plot saved results](../workflows/saved-results.md) · [Next: Diagnostics and sensitivity](diagnostics.md)
