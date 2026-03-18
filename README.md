# A/B Test — Enterprise Feature Analysis

Simulates and analyzes a two-sided A/B experiment modeled on an enterprise SaaS feature launch. The dataset is synthetic with controlled ground truth, so the "right answer" is known — which makes it possible to evaluate whether the statistical methods actually work.

Built this to practice end-to-end experimentation: from sample size planning through sequential monitoring and a ship/kill decision.

## What it does

Generates 3,000 synthetic users split evenly into control and treatment. The treatment group gets a higher activation probability and a session lift baked into the data generator — so there's a real signal to detect.

From there, the analysis runs:

- **Two-proportion z-test** — primary test for activation rate lift
- **Welch's t-test + Cohen's d** — session engagement, handles unequal variance
- **Chi-square test** — robustness check; same question, different method
- **O'Brien-Fleming sequential monitoring** — 10 interim looks with tightening boundaries to catch early stopping bias

## Results

| Metric | Control | Treatment | Lift | Significant |
|---|---|---|---|---|
| Activation rate | 20.3% | 28.5% | +8.2 pp | Yes (p ≈ 0) |
| Sessions per user | 4.21 | 5.18 | +0.96 | Yes (d = 0.46) |

The z-stat crossed the OBF boundary at look 3 (30% enrolled), but given that this is synthetic data with a known lift, the more interesting check is that the boundary held correctly early — look 1 and 2 both stayed below it despite the real effect.

## Concepts demonstrated

- Power analysis and sample size planning
- Effect size: Cohen's d, Cohen's h, Cramér's V
- Multiple comparison correction (Bonferroni)
- Sequential monitoring with O'Brien-Fleming spending function
- Ship / iterate / kill framing based on effect size + significance

## Stack

Python · NumPy · pandas · SciPy · statsmodels · matplotlib

## Setup
```bash
pip install -r requirements.txt
jupyter notebook data_generator.ipynb
```
```

---

**requirements.txt**
```
numpy>=1.24
pandas>=2.0
scipy>=1.11
statsmodels>=0.14
matplotlib>=3.7
jupyter>=1.0
```

---

**Power analysis cell** — paste this as a new cell near the top of the notebook, before the data generation, with a markdown header above it:

Markdown cell:
```
## Stage 0: Power Analysis — How Many Users Do We Need?

Before running the experiment, we need to know how large a sample is required to reliably detect the effect we care about. Too small and we'll miss real effects. Too large and we're wasting experiment time.

We're targeting an 8 pp lift (0.22 → 0.30 baseline), with 80% power and α = 0.05.
