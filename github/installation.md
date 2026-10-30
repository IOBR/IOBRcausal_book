<!-- Generated from installation.qmd. Edit the QMD source and rebuild. -->

# Installation

[Book contents](../README.md) · [Previous: IOBRcausal](index.md) · [Next: Your first analysis](quick-start.md)

## Install the R package

Use R 4.1 or later and Git. In R, run:

```r
if (!requireNamespace("remotes", quietly = TRUE)) install.packages("remotes")
remotes::install_git(
  "https://github.com/IOBR/IOBRcausal.git",
  git = "external", upgrade = "never"
)
library(IOBRcausal)
packageVersion("IOBRcausal")
find.package("IOBRcausal")
```

Git uses your existing repository credentials. If the repository is restricted,
your GitHub account needs access. A successful Skill installation does not update
the R package; check the version and loaded path after restarting R.

On Windows, run the code in RStudio or R. If a dependency needs compilation,
install the Rtools version matching your R installation. On Linux, use your
normal R library and ask the system administrator for any missing compiler or
system library reported by a dependency.

Already have the source folder? From its root, install it with:

```r
install.packages(".", repos = NULL, type = "source")
```

## Install the Skill

The Skill is optional. With Node.js 22.20 or later and Git, run this in a terminal:

```bash
npx --yes skills@1.7.4 add https://github.com/IOBR/IOBRcausal/tree/main/inst/IOBRcausalSkill --agent codex --global --copy --yes
```

For Claude Code, replace `codex` with `claude-code`. The command installs
instructions. Analysis also needs R and IOBRcausal. Repository credentials may
be needed on a server as well as on Windows.

The same Skill documents travel inside the R package:

```r
system.file("IOBRcausalSkill", package = "IOBRcausal")
```

Start a new host session after installation. See the [Skill guide](agent-guide.md)
for task examples and optional package-managed integration.

## Check the installation

```r
teaching <- read.csv(system.file(
  "extdata", "iobrcausal_teaching_iobr.csv", package = "IOBRcausal"
))
check <- causal_glm(
  teaching, "T_cell_inflamed_score", "Response",
  confounders = c("Age", "Sex", "ECOG"), outcome_type = "binary"
)
check[, c("Method", "Scale", "Estimate", "CI_L", "CI_U", "P_value")]
```

This small installation check returns a Log-OR for the continuous score. It is
separate from the full workflow in [your first analysis](quick-start.md).
For errors, see [troubleshooting](reference/troubleshooting.md).

---

[Book contents](../README.md) · [Previous: IOBRcausal](index.md) · [Next: Your first analysis](quick-start.md)
