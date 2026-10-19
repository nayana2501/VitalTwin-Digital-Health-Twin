import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from src.twin_engine import build_twin, simulate_intervention, generate_history

st.set_page_config(page_title="VitalTwin | Healthcare Digital Twin", page_icon="🫀", layout="wide")
st.title("🫀 VitalTwin — Personal Health Digital Twin")
st.caption("A privacy-first educational prototype that simulates how lifestyle changes may influence selected wellness indicators. Not a medical device.")

with st.sidebar:
    st.header("Twin profile")
    age = st.slider("Age", 18, 85,  thirty if False else 30)
    activity = st.slider("Activity (minutes/day)", 0, 120, 30)
    sleep = st.slider("Sleep (hours/night)", 3.0, 12.0, 7.0, 0.5)
    stress = st.slider("Perceived stress", 1, 10, 5)
    resting_hr = st.slider("Resting heart rate (bpm)", 45, 120, 72)
    systolic = st.slider("Systolic blood pressure (mmHg)", 85, 200, 122)
    hydration = st.slider("Water intake (litres/day)", 0.5, 5.0, 2.0, 0.25)
    st.divider()
    st.caption("Use fictional/example inputs only. Do not enter identifiable patient data.")

profile = {"age": age, "activity": activity, "sleep": sleep, "stress": stress,
           "resting_hr": resting_hr, "systolic": systolic, "hydration": hydration}
twin = build_twin(profile)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Wellness index", f"{twin['wellness_index']}/100", twin["wellness_label"])
c2.metric("Resting heart rate", f"{resting_hr} bpm")
c3.metric("Sleep", f"{sleep:.1f} h/night")
c4.metric("Activity", f"{activity} min/day")

st.subheader("Your current digital twin")
left, right = st.columns([1.2, 1])
with left:
    hist = generate_history(profile, days=30)
    fig = px.line(hist, x="day", y=["wellness_index", "sleep_score", "activity_score"],
                  title="Illustrative 30-day wellness trajectory", labels={"value":"Score", "day":"Day", "variable":"Indicator"})
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.markdown("#### What is influencing the twin?")
    factors = pd.DataFrame({"Factor": list(twin["contributions"].keys()),
                            "Contribution": list(twin["contributions"].values())})
    fig2 = px.bar(factors.sort_values("Contribution"), x="Contribution", y="Factor", orientation="h",
                  title="Transparent model contributions")
    st.plotly_chart(fig2, use_container_width=True)

st.info("The wellness index is a prototype score created from user-entered lifestyle values; it is not a clinical risk score and cannot diagnose or predict disease.")

st.subheader("Intervention sandbox")
st.write("Change hypothetical habits and compare the simulated twin. These are scenario illustrations, not guaranteed outcomes.")
a, b, c = st.columns(3)
with a:
    extra_activity = st.slider("Additional activity (min/day)", 0, 60, 15, 5)
with b:
    extra_sleep = st.slider("Additional sleep (hours/night)", 0.0, 2.0, 0.5, 0.5)
with c:
    stress_change = st.slider("Stress reduction (points)", 0, 5, 1)

scenario = simulate_intervention(profile, extra_activity, extra_sleep, stress_change)
x, y, z = st.columns(3)
x.metric("Current index", f"{twin['wellness_index']}/100")
y.metric("Scenario index", f"{scenario['wellness_index']}/100",
         delta=f"{scenario['wellness_index'] - twin['wellness_index']} points")
z.metric("Scenario label", scenario["wellness_label"])

compare = pd.DataFrame([
    {"Scenario":"Current twin", "Wellness index":twin["wellness_index"]},
    {"Scenario":"Hypothetical intervention", "Wellness index":scenario["wellness_index"]}
])
st.plotly_chart(px.bar(compare, x="Scenario", y="Wellness index", range_y=[0,100],
                       title="Current vs hypothetical scenario"), use_container_width=True)

st.subheader("Suggested next steps")
for tip in twin["suggestions"]:
    st.write(f"• {tip}")
st.caption("If you have symptoms or concerns about blood pressure or heart rate, seek guidance from a qualified healthcare professional. Do not use this demo to change medication or treatment.")
