"""Transparent, rule-based wellness twin engine. Not intended for clinical use."""
import numpy as np
import pandas as pd

def _clip(value, low=0, high=100):
    return max(low, min(high, float(value)))

def build_twin(profile):
    # Normalized component scores are deliberately simple and explainable.
    activity_score = _clip(profile["activity"] / 60 * 100)
    sleep_score = _clip(100 - abs(profile["sleep"] - 8) * 18)
    stress_score = _clip(100 - (profile["stress"] - 1) * (100 / 9))
    hr_score = _clip(100 - abs(profile["resting_hr"] - 65) * 1.6)
    bp_score = _clip(100 - max(0, profile["systolic"] - 115) * 1.4 - max(0, 95 - profile["systolic"]) * 0.8)
    hydration_score = _clip(100 - abs(profile["hydration"] - 2.5) * 22)
    weights = {"Activity": .22, "Sleep": .22, "Stress": .18, "Resting heart rate": .14,
               "Systolic BP": .14, "Hydration": .10}
    scores = [activity_score, sleep_score, stress_score, hr_score, bp_score, hydration_score]
    score = round(sum(s*w for s,w in zip(scores, weights.values())))
    label = "Strong habits" if score >= 80 else "Room to improve" if score >= 60 else "Consider support"
    contributions = {k: round(v*w, 1) for (k,w),v in zip(weights.items(), scores)}
    suggestions = []
    if profile["activity"] < 30:
        suggestions.append("Consider adding gentle movement in a way that feels safe and sustainable.")
    if profile["sleep"] < 7:
        suggestions.append("Consider a consistent sleep and wake schedule.")
    if profile["stress"] >= 7:
        suggestions.append("Try a short relaxation break or talk with someone you trust about stress.")
    if profile["hydration"] < 1.5:
        suggestions.append("Review hydration needs, taking your activity and climate into account.")
    if profile["systolic"] >= 130:
        suggestions.append("A single blood-pressure value is not a diagnosis; consider repeating measurements correctly and discussing persistent high readings with a clinician.")
    if not suggestions:
        suggestions.append("Keep tracking your habits over time and focus on small, realistic changes.")
    return {"wellness_index": int(_clip(score)), "wellness_label": label,
            "components": dict(zip(weights.keys(), [round(s) for s in scores])),
            "contributions": contributions, "suggestions": suggestions}

def simulate_intervention(profile, extra_activity=0, extra_sleep=0, stress_reduction=0):
    updated = dict(profile)
    updated["activity"] = min(120, updated["activity"] + extra_activity)
    updated["sleep"] = min(12, updated["sleep"] + extra_sleep)
    updated["stress"] = max(1, updated["stress"] - stress_reduction)
    return build_twin(updated)

def generate_history(profile, days=30):
    """Synthetic illustrative history anchored around current profile, with deterministic seed."""
    rng = np.random.default_rng(42)
    current = build_twin(profile)["wellness_index"]
    day = np.arange(1, days+1)
    wellness = np.clip(current + np.linspace(-6, 0, days) + rng.normal(0, 2, days), 0, 100)
    sleep = np.clip(75 + (profile["sleep"]-7)*8 + rng.normal(0, 4, days), 0, 100)
    activity = np.clip(profile["activity"]/60*100 + rng.normal(0, 5, days), 0, 100)
    return pd.DataFrame({"day":day, "wellness_index":wellness.round(1),
                         "sleep_score":sleep.round(1), "activity_score":activity.round(1)})
