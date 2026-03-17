# A/B Testing — Enterprise Feature Analysis

Simulates and analyzes A/B experiments modeled on enterprise SaaS feature launches.
Built from scratch to demonstrate end-to-end experimentation methodology.

## What it does
- Generates synthetic user-level experiment data with controlled ground truth
- Tests activation rate lift using a two-proportion z-test
- Measures session engagement change using Welch's t-test and Cohen's d
- Validates results with chi-square test as a robustness check
- Implements O'Brien-Fleming sequential monitoring to prevent early stopping bias

## Results
| Metric | Control | Treatment | Lift | Significant |
|---|---|---|---|---|
| Activation rate | 20.3% | 28.5% | +8.2 pp | Yes (p≈0) |
| Sessions per user | 4.21 | 5.18 | +0.96 | Yes (d=0.46) |

## Key concepts demonstrated
- Power analysis and sample size planning
- Effect size measurement (Cohen's d, Cohen's h, Cramér's V)
- Multiple comparison correction (Bonferroni)
- Sequential monitoring with O'Brien-Fleming boundaries
- Ship / iterate / kill decision framework

## Stack
Python · NumPy · pandas · SciPy · statsmodels · matplotlib
