<!-- Generated from reference/parameters.qmd. Edit the QMD source and rebuild. -->

# Parameters and analysis settings

[Book contents](../../README.md) · [Previous: Use the IOBRcausal Skill](../agent-guide.md) · [Next: Function reference](functions.md)

Decide the endpoint, exposure contrast, covariates and testing family before
changing performance or screening settings. Keep the effective request with
the result so another reader can see what was actually used.

## The shared request

The [workflow examples](../workflows/pathway-first.md) use explicit route,
features where applicable, endpoints, methods and parameters. A complete
workflow sets `parameters$complete_workflow = TRUE`; use `plan_only = TRUE`
to inspect the request before an execution you have not yet agreed.

| Setting | Purpose |
| --- | --- |
| `workflow` | Choose `pathway_first` or `exposure_first` |
| `features` | Exact named features for exposure-first |
| `endpoints` | Binary endpoint and/or time, event status, event code and units |
| `covariates` | Agreed baseline adjustment variables |
| `methods` | Requested estimator set; support filtering remains explicit |
| `parameters$seed` | Reproducible random settings |
| `parameters$profile` | A supported settings profile |
| `parameters$complete_workflow` | Request the full analysis-to-delivery route |

## Direct R control objects

Advanced direct workflow APIs can use `iobr_causal_control()`:

```r
ctrl <- iobr_causal_control(
  profile = "standard",
  screening = list(top_n = 30, fdr_threshold = 0.15),
  estimation = list(boot_R = 500, boot_parallel = TRUE, boot_ncpus = 4)
)
```

Use the relevant function's help for its `control` argument. This object is not
an instruction to run a second backend after a complete shared request.

Profiles provide defaults, not study-specific justification. A broad screening
FDR gate is not a universal threshold for final claims. Formal OS mediation
under a frozen project protocol has its own fixed model and family rules.

## Exposure and survival contrasts

Direct estimator wrappers expose selected options. The core
`iobr_causal_estimate()` additionally accepts `effect_spec` for bootstrap,
continuous intervention and survival target settings. For example,
`forest_num_trees` is the core setting behind the forest wrapper's `num_trees`.
The default survival target is RMST difference; Cox summaries require an explicit
`hazard_ratio` target. A fixed-horizon survival probability contrast is separate.

Specify policies, dose contrasts and horizons from the scientific question and
observed support. A wrapper does not expose every advanced setting. Keep primary
settings fixed and label sensitivity analyses separately.


## Detailed control dictionary

| Parameter | Controls | Increase means | Decrease means |
|---|---|---|---|
| `top_n` | how many ranked candidates move forward | broader review | fewer candidates |
| `fdr_threshold` | FDR gate for candidate highlighting | more permissive | more conservative |
| `p_threshold` | nominal P reference | more exploratory signals | fewer nominal signals |
| `missing_threshold` | allowed missing fraction | keeps more incomplete variables | removes incomplete variables earlier |
| `min_abundance` | value required for one matched sample to count as detected | requires more abundance | counts lower values as detected |
| `min_prevalence` | fraction of matched samples that must be detected | removes more rare features | keeps rarer features |
| `min_complete_rate` | complete-case fraction | stricter data support | more permissive |
| `min_orr_n` | ORR complete-case N | blocks small ORR scans | allows smaller ORR scans |
| `min_survival_n` | survival complete-case N | blocks small survival scans | allows smaller survival scans |
| `min_group_n` | each binary group size | stricter group support | allows rare groups |
| `min_event_n` | survival event count | stricter survival evidence | allows event-sparse scans |
| `boot_R` | bootstrap repetitions | more stable, slower | faster, noisier |
| `boot_parallel` | multiple CPU workers for candidate screening and bootstrap-backed estimators | faster screening/formal estimation, more memory use | single-process execution |
| `boot_ncpus` | requested CPU worker count | usually faster, more memory use | lower memory use, slower |
| `ipw_truncate` | IPW weight trimming | wider range trims less | narrower range trims more |
| `psm_caliper` | matching tolerance | more matches, looser | fewer matches, tighter |
| `ph_p_warn` | PH warning threshold | usually keep at 0.05 | usually keep at 0.05 |
| `censor_rate_warn` | censoring warning cutoff | more tolerant | stricter |
| `ess_ratio_warn` | effective sample warning | more tolerant if lower | stricter if higher |

---

[Book contents](../../README.md) · [Previous: Use the IOBRcausal Skill](../agent-guide.md) · [Next: Function reference](functions.md)
