<!-- Generated from reference/functions.qmd. Edit the QMD source and rebuild. -->

# Function reference

[Book contents](../../README.md) · [Previous: Parameters and analysis settings](parameters.md) · [Next: Troubleshooting](troubleshooting.md)

Use the workflow chapters for complete analysis delivery. This map preserves
the detailed public function guide for direct R lookup. Open `?function_name`
in R for the exact interface in your installed version.

## How To Use This Page

This map is organized by user goal, not by source file. Internal helpers are
not included. Start with the goal that matches your task.

## Data Preparation

| Function | Use when | Output | New user? | Boundary |
|---|---|---|---|---|
| `iobr_causal_load()` | load clinical/signature data into CausalData | CausalData | yes | data prep only |
| `causal_from_iobr()` | bridge IOBR objects/results | CausalData-like object | yes | bridge, not evidence |
| `iobr_causal_impute()` | impute missing values in CausalData | imputed CausalData | cautious | imputation adds assumptions |

## Main Workflow

| Function | Use when | Output | New user? | Boundary |
|---|---|---|---|---|
| `iobr_causal_pathway_first_workflow()` | expression plus clinical data; default scientific main route | pathway and gene endpoint reports | yes, start here | pathway evidence, not mechanism proof |
| `iobr_causal_gene_set_sources()` | none | supported source/license table | before external retrieval | availability and license boundary only |
| `iobr_causal_get_gene_sets()` | source plus optional pathway names | named gene sets or audited resource | pathway-first input preparation | database content, not pathway evidence |
| `iobr_causal_match_gene_sets()` | pathway names plus gene sets | conservative match audit | reconcile score and gene-set names | no unrestricted fuzzy matching |
| `iobr_causal_map_gene_ids()` | human gene identifiers | mapping audit table | identifier preparation | mapping is not expression QC |
| `iobr_causal_pathway_first_rules()` | configure pathway and mapped-gene gates | evidence rules | yes | user-configurable prioritization rules |
| `iobr_causal_validate_main_route()` | verify known-truth recovery, parameter reach, parallel parity, and reference agreement | validation tables | maintainer/reviewer | software QA, not external biological validation |
| `iobr_causal()` | run a general high-level workflow | workflow result | secondary | still assumption-bound |
| `causal_pipeline()` | flexible causal pipeline | pipeline result | intermediate | not automatic proof |
| `iobr_causal_exposure_first_workflow()` | prespecified/precomputed feature table | exposure-level reports | secondary | no pathway-to-gene discovery |

Pathway-first is the organizing main line. Candidate screening, formal-method
extensions, survival special cases, prediction, visualization, AI, and audit
support that line or answer narrower questions; they do not replace it.

## Parameter Control

| Function | Use when | Output | New user? | Boundary |
|---|---|---|---|---|
| `iobr_causal_control()` | set thresholds/methods in one object | control object | yes | parameters must be reported |
| `iobr_causal_control_reference()` | explain parameters | data frame | yes | explanation only |

## Secondary Candidate Screening

| Function | Use when | Output | New user? | Boundary |
|---|---|---|---|---|
| `iobr_causal_define_exposure_pool()` | define candidate features | exposure pool | intermediate | not evidence |
| `iobr_causal_prefilter_exposures()` | remove unusable candidates | prefilter result | intermediate | quality control |
| `iobr_causal_scan_exposures()` | scan candidates against endpoint | scan table | intermediate | screening only |
| `iobr_causal_candidate_gate()` | select candidates for formal review | gate table | yes | gate, not conclusion |
| `iobr_causal_intersect_exposures()` | find ORR/survival overlap | intersection table | yes | priority only |
| `iobr_causal_candidate_workflow()` | run staged workflow on prespecified features | workflow + Excel outputs | secondary | candidate entry, not pathway-first replacement |
| `iobr_causal_longitudinal_candidate_scan()` | scan longitudinal candidates | scan result | advanced | exploratory unless supported |

## Formal Estimation

| Function | Use when | Output | New user? | Boundary |
|---|---|---|---|---|
| `iobr_causal_estimate()` | estimate effect from CausalData | estimate result | yes | under declared assumptions |
| `iobr_causal_formal_estimate_candidates()` | estimate selected candidates | formal candidate table | yes | not multi-method proof by default |
| `causal_glm()` | GLM estimate | estimate table | yes | model-based |
| `causal_gcomp()` | g-computation | estimate table | yes | model-based standardization |
| `causal_ipw()` | inverse probability weighting | estimate table | advanced | check weights/ESS |
| `causal_psm()` | propensity score matching | matched estimate | advanced | check match quality |
| `causal_tmle()` | TMLE | estimate table | advanced | dependency/assumption sensitive |
| `causal_aipw()` | doubly robust AIPW | estimate table | advanced | needs diagnostics |
| `causal_dml()` | double machine learning | estimate table | advanced | needs careful review |
| `causal_gps()` | continuous exposure GPS | estimate table | advanced | continuous exposure assumptions |
| `causal_forest_estimate()` | heterogeneity ranking | HTE result | advanced | not individualized proof |
| `causal_compare_all()` | compare methods | method comparison | intermediate | comparison, not consensus proof |
| `compare_methods()` | summarize method results | table | intermediate | display utility |

## Feature, Discovery, DAG

| Function | Use when | Output | New user? | Boundary |
|---|---|---|---|---|
| `iobr_causal_feature()` | select features | selected features | intermediate | feature selection only |
| `causal_select()` | single feature selection method | selection result | intermediate | screening |
| `causal_select_ensemble()` | ensemble feature selection | selection result | advanced | screening |
| `iobr_causal_discover()` | DAG/causal discovery | discovery result | advanced | diagnostic only |
| `causal_discover_single()` | one discovery method | graph result | advanced | not proof of identification |
| `causal_discover_ensemble()` | ensemble discovery | graph result | advanced | support, not proof |
| `iobr_causal_validate_adjustment()` | review adjustment set | validation result | advanced | adjustment-boundary review |
| `causal_check_adjustment()` | check DAG adjustment | validation result | advanced | DAG-dependent |
| `dag_evaluate()` | evaluate discovery output | diagnostic table | advanced | diagnostic |

## Survival

| Function | Use when | Output | New user? | Boundary |
|---|---|---|---|---|
| `iobr_causal_survival_report()` | standard survival report | survival report | yes | check PH/censoring |
| `iobr_causal_survival_platform_report()` | unified survival report | platform report | yes | stable/extended scopes differ |
| `iobr_causal_survival_diagnostics()` | survival diagnostics | diagnostic table | yes | diagnostic |
| `survival_diagnostics()` | time-to-event diagnostics | diagnostic table | yes | diagnostic |
| `iobr_causal_survival_rmst()` | RMST summary | RMST table | intermediate | horizon-specific |
| `iobr_causal_survival_milestone()` | milestone survival | milestone table | intermediate | timepoint-specific |
| `iobr_causal_survival_competing_risks()` | competing risk summary | competing risk result | advanced | competing event assumptions |
| `iobr_causal_survival_competing_report()` | competing risk report | report | advanced | bounded |
| `iobr_causal_survival_vnext_report()` | extended survival family report | vNext report | advanced | research/extended |
| `iobr_causal_survival_unified_report()` | alias for unified report | report | yes | same as platform |
| `iobr_causal_survival_final_summary()` | alias for final report | report | yes | compatibility |
| `iobr_causal_survival_maximal_report()` | maximal survival report alias | report | advanced | compatibility |

## Advanced Survival Families

| Family | Functions | Boundary |
|---|---|---|
| longitudinal survival | `iobr_causal_survival_longitudinal_prepare()`, `iobr_causal_survival_msm()`, `iobr_causal_survival_gformula()`, `iobr_causal_survival_regime_compare()`, `iobr_causal_survival_regime_engine()` | advanced, assumption-heavy |
| dynamic regimes | `iobr_causal_survival_dynamic_regimes_prepare()`, `iobr_causal_survival_dynamic_regime_compare()` | prototype/policy review unless supported |
| longitudinal competing risks | `iobr_causal_survival_longitudinal_competing_prepare()`, `iobr_causal_survival_longitudinal_competing_msm()`, `iobr_causal_survival_longitudinal_competing_gformula()`, `iobr_causal_survival_longitudinal_competing_report()` | advanced |
| multistate | `iobr_causal_survival_multistate_prepare()`, `iobr_causal_survival_multistate_summary()`, `iobr_causal_survival_multistate_causal_prepare()`, `iobr_causal_survival_multistate_causal_estimate()`, `iobr_causal_survival_multistate_report()` | semi-causal/advanced |
| policy learning | `iobr_causal_survival_policy_prepare()`, `iobr_causal_survival_policy_learn()`, `iobr_causal_survival_policy_evaluate()`, `iobr_causal_survival_policy_report()` | prototype/exploratory unless support says otherwise |
| time-local | `iobr_causal_survival_time_local()` | local time summary |

## Sensitivity And Diagnostics

| Function | Use when | Output | Boundary |
|---|---|---|---|
| `iobr_causal_sensitivity()` | robustness supplement | sensitivity result | not proof of no confounding |
| `causal_ps_check()` | propensity/balance check | diagnostics | support review |
| `causal_evaluate()` | conservative result evaluation | evaluation | not a new estimate |
| `causal_summary()` | summarize estimates | summary | display |

## Interpretation

| Function | Use when | Output |
|---|---|---|
| `iobr_causal_readout()` | user-friendly result readout | text/list readout |
| `iobr_causal_contract()` | normalize result contract | contract object |
| `iobr_causal_interpret()` | unified interpretation helper | interpretation |
| `interpret_estimate()` | estimate-specific interpretation | interpretation |
| `interpret_survival()` | survival-specific interpretation | interpretation |
| `interpret_discovery()` | discovery/DAG interpretation | interpretation |
| `interpret_validation()` | validation interpretation | interpretation |
| `interpret_hte()` | heterogeneity interpretation | interpretation |

## Excel, Artifacts, Audit

| Function | Use when | Output |
|---|---|---|
| `iobr_causal_read_result_bundle()` | read Excel/result directory | bounded readout |
| `iobr_causal_write_audit_summary()` | summarize an existing audit folder | audit summary |
| `iobr_causal_artifacts()` | list artifacts | artifact table |
| `iobr_causal_audit()` | audit claim/method/rerun surfaces | audit table |
| `iobr_causal_method_provenance()` | explain method source | provenance table |
| `iobr_causal_freeze_protocol()` | freeze protocol | protocol file/list |
| `iobr_causal_rerun_recipe()` | show rerun recipe | recipe |
| `iobr_causal_log()` | view/export log | log table/file |
| `iobr_causal_selftest()` | package self-test | test results |

## Visualization

| Function | Use when |
|---|---|
| `iobr_causal_plot()` | one contract-aware plot |
| `iobr_causal_visual_report()` | ordered figure set |
| `plot_clinical_summary()` | clinical-style summary figure |
| `plot_clinical_implications()` | clinical implication summary |

Ordinary users should choose plot surfaces through `iobr_causal_plot(type = ...)`.
For example, use `type = "forest"`, `"love"`, `"screening"`, `"sensitivity"`,
or `"survival"`. Lower-level plot helpers are implementation details unless
they are exported in the installed namespace.

## AI and Agent Entry

| Function | Use when |
|---|---|
| `iobrcausal()` | structured requests, configured natural language, or interactive R |

CLI/MCP use the same request dispatcher. Provider and registry helpers are internal.

## Platform Design Families

| Function | Use when | Boundary |
|---|---|---|
| `iobr_causal_iv_report()` | instrumental-variable/LATE design | IV assumptions required |
| `iobr_causal_did_report()` | difference-in-differences design | parallel trends review |
| `iobr_causal_rdd_report()` | regression discontinuity design | local cutoff/bandwidth review |

These are design-family reports. Do not describe them as ordinary adjusted
observational estimates.

---

[Book contents](../../README.md) · [Previous: Parameters and analysis settings](parameters.md) · [Next: Troubleshooting](troubleshooting.md)
