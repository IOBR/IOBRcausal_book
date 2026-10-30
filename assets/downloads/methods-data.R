# Synthetic data for the Book's direct R estimator examples.
# Fictional treatment, biomarkers and outcomes; no patient data are used.
set.seed(20261030)
n <- 240L
Age <- stats::rnorm(n, 62, 8)
Sex <- sample(c("F", "M"), n, replace = TRUE)
Stage <- sample(c("II", "III", "IV"), n, replace = TRUE)
ECOG <- sample(0:2, n, replace = TRUE)
Immunotherapy <- stats::rbinom(n, 1, stats::plogis(-0.3 + 0.03 * (Age - 62) - 0.2 * ECOG))
TMB <- exp(stats::rnorm(n, 1 + 0.01 * (Age - 62), 0.5))
Response <- stats::rbinom(n, 1, stats::plogis(
  -0.7 + 0.6 * Immunotherapy - 0.2 * ECOG + 0.15 * log(TMB)
))
TumorChange <- 0.8 * Immunotherapy + 0.02 * (Age - 62) + stats::rnorm(n)
event_time <- stats::rexp(n, rate = exp(-0.35 * Immunotherapy + 0.15 * ECOG) / 18)
censor_time <- stats::rexp(n, rate = 1 / 30)
data <- data.frame(
  ID = sprintf("DEMO%03d", seq_len(n)), Immunotherapy, TMB, Age, Sex, Stage, ECOG,
  Response, TumorChange, OS_months = pmin(event_time, censor_time),
  OS_event = as.integer(event_time <= censor_time)
)
