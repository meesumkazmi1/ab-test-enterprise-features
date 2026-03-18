# A/B Test — Enterprise Feature Analysis

Simulates and analyzes a two-sided A/B experiment modeled on an enterprise SaaS feature launch. The dataset is synthetic with controlled ground truth — meaning the right answer is known upfront, which makes it possible to verify that the statistical methods actually detect what they should.

Built to practice end-to-end experimentation: from sample size planning through sequential monitoring and a ship/kill decision.

## What it does

Generates 3,000 synthetic users split evenly into control and treatment. The treatment group gets a higher activation probability and a session lift baked into the data generator — so there's a real signal to find.

The analysis runs in stages:

1. **Power analysis** — justifies the sample size before any data is generated
2. **Two-proportion z-test** — primary test for activation rate lift
3. **Welch's t-test + Cohen's d** — session engagement, using Welch's variant since it doesn't assume equal variance
4. **Chi-square + Cramér's V** — robustness check; same hypothesis as the z-test, different method, easier effect size to communicate to non-technical stakeholders
5. **O'Brien-Fleming sequential monitoring** — 10 interim looks with tightening early-stopping boundaries
6. **Ship / iterate / kill decision** — combines significance with minimum effect size thresholds

## Results

| Metric | Control | Treatment | Lift | Significant |
|---|---|---|---|---|
| Activation rate | 20.3% | 28.5% | +8.2 pp | Yes (p ≈ 0) |
| Sessions per user | 4.21 | 5.18 | +0.96 | Yes (d = 0.46) |

The z-stat crossed the OBF boundary at look 3 (30% enrolled). Looks 1 and 2 stayed below the boundary despite a real effect being present — exactly the behavior OBF is designed to produce.

## Stack

Python · NumPy · pandas · SciPy · statsmodels · matplotlib

## Setup

```bash
pip install -r requirements.txt
jupyter notebook ab_test_analysis.ipynb
```
