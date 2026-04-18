import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="AI Guardrail Demo", layout="wide")

# Title and Context
st.title("🛡️ AI Confidence vs. Guardrail Simulator")
st.info("Demo for Rayda PM Assessment - Created by Victor Anderson")

# Sidebar - These are your "Knobs" for the interview
st.sidebar.header("Decision Parameters")
threshold = st.sidebar.slider("AI Confidence Threshold (%)", 50, 99, 85)
st.sidebar.markdown("""
**The Logic:**
The AI only automates a request if its internal confidence score is higher than this threshold. 
""")

# Simulation Data Logic
total_requests = 1000
np.random.seed(42)
scores = np.random.normal(78, 12, total_requests)

# Calculations
automated_reqs = scores[scores > threshold]
automation_rate = len(automated_reqs) / total_requests
# Error rate logic: Lower threshold = higher chance of wrong resolution (re-opens)
error_rate = max(1.5, (100 - threshold) * 0.4) 
reopens = int(len(automated_reqs) * (error_rate / 100))

# Display Metrics
col1, col2, col3 = st.columns(3)
col1.metric("North Star: Automation Rate", f"{automation_rate:.1%}", help="Target: 30%")
col2.metric("Guardrail: Re-open Rate", f"{error_rate:.1f}%", delta=f"{reopens} tickets", delta_color="inverse")

if error_rate > 10:
    col3.error("🚨 HIGH RISK: Trust Erosion")
elif error_rate > 5:
    col3.warning("⚠️ CAUTION: Monitor Feedback")
else:
    col3.success("✅ HEALTHY: High Trust")

# Visualizing the Trade-off
st.write("---")
st.subheader("Automation Volume vs. Quality Risk")

chart_data = pd.DataFrame({
    "Threshold %": list(range(50, 100)),
    "Automation Volume": [len(scores[scores > t]) for t in range(50, 100)],
    "Risk of Re-open": [max(1.5, (100 - t) * 0.4) * 5 for t in range(50, 100)] # Scaling for visual
})

st.line_chart(chart_data.set_index("Threshold %"))

st.markdown("""
**Victor's Defense Strategy:**
* **Low Threshold:** Moves the North Star (Automation) up, but breaks the Guardrail (Re-opens).
* **High Threshold:** Protects the Guardrail, but misses the North Star.
* **The Goal:** Use the 90-day Beta to find the 'Sweet Spot' (usually 85-90%).
""")
