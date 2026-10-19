from src.twin_engine import build_twin, simulate_intervention

PROFILE = {"age": 30, "activity": 20, "sleep": 6.0, "stress": 7,
           "resting_hr": 75, "systolic": 132, "hydration": 1.5}

def test_score_is_bounded():
    result = build_twin(PROFILE)
    assert 0 <= result["wellness_index"] <= 100

def test_intervention_does_not_reduce_score_for_this_profile():
    current = build_twin(PROFILE)["wellness_index"]
    future = simulate_intervention(PROFILE, extra_activity=20, extra_sleep=1, stress_reduction=2)["wellness_index"]
    assert future >= current

def test_explanations_present():
    result = build_twin(PROFILE)
    assert result["contributions"]
    assert result["suggestions"]
