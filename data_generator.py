"""
data_generator.py
-----------------
Synthetic data generator for the A/B experiment.

Generates user-level experiment data with controlled ground truth —
meaning the true lift is baked in, so statistical methods can be
evaluated against a known answer.

Usage:
    from data_generator import ExperimentData
    gen = ExperimentData(seed=42)
    df = gen.generate()
"""

import numpy as np
import pandas as pd


class ExperimentData:
    """
    Simulates user-level A/B experiment data.

    Parameters
    ----------
    seed : int
        Random seed for reproducibility.
    """

    def __init__(self, seed: int = 42):
        self.rng = np.random.default_rng(seed)

    def generate(
        self,
        n_per_group: int = 1500,
        baseline_rate: float = 0.22,
        true_lift: float = 0.08,
        baseline_sessions: tuple = (4.2, 2.1),
        session_lift: float = 0.9,
    ) -> pd.DataFrame:
        """
        Generate synthetic experiment data.

        Parameters
        ----------
        n_per_group : int
            Number of users per group (control and treatment).
        baseline_rate : float
            Activation probability for control group.
        true_lift : float
            Additional activation probability for treatment group.
        baseline_sessions : tuple
            (mean, std) of session count for control group.
        session_lift : float
            Mean session count added for treatment group.

        Returns
        -------
        pd.DataFrame
            Columns: user_id, group, activated, sessions
        """
        n = n_per_group * 2
        groups = ["control"] * n_per_group + ["treatment"] * n_per_group
        self.rng.shuffle(groups)

        activation_prob = [
            baseline_rate + true_lift if g == "treatment" else baseline_rate
            for g in groups
        ]
        activated = self.rng.binomial(1, activation_prob)

        mu, sigma = baseline_sessions
        sessions = self.rng.normal(mu, sigma, size=n)
        treat_mask = np.array([g == "treatment" for g in groups])
        sessions[treat_mask] += session_lift
        sessions = np.maximum(sessions, 0).round(1)

        return pd.DataFrame(
            {
                "user_id": range(n),
                "group": groups,
                "activated": activated,
                "sessions": sessions,
            }
        )


if __name__ == "__main__":
    gen = ExperimentData(seed=42)
    df = gen.generate()

    print(f"Total users:  {len(df)}")
    print(f"Control:      {(df['group'] == 'control').sum()}")
    print(f"Treatment:    {(df['group'] == 'treatment').sum()}")
    print()
    print(df.groupby("group")[["activated", "sessions"]].mean().round(4))
    print()
    print(df.head())
