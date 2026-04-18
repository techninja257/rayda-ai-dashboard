import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(page_title="Victor Anderson | Rayda Assessment", layout="wide")

# --- CUSTOM CSS (IMPROVED CONTRAST FOR CARDS) ---
st.markdown("""
    <style>
    /* Metric Card Styling */
    [data-testid="stMetric"] {
        background-color: #000000 !important;
        padding: 20px !important;
        border-radius: 12px !important;
        border: 1px solid #333333 !important;
        color: white !important;
    }
    
    /* Force Label & Value to White */
    [data-testid="stMetricLabel"] > div {
        color: #FFFFFF !important;
        font-weight: bold !important;
    }
    [data-testid="stMetricValue"] > div {
        color: #FFFFFF !important;
    }
    
    /* Optional: Improve general UI padding */
    .main .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Victor Anderson: PM Assessment")
page = st.sidebar.radio("Select Task Demo:", ["🖥️ Client Trust Portal (Task 1)", "📈 AI Strategy & Metrics (Task 2)"])

st.sidebar.divider()
st.sidebar.info("Pro Tip: During the call, use the sidebar to toggle between 'Client Experience' and 'Internal Strategy'.")

# ==========================================
# PAGE 1: CLIENT TRUST PORTAL (TASK 1)
# ==========================================
if page == "🖥️ Client Trust Portal (Task 1)":
    st.title("🖥️ Task 1: Enterprise Request Tracking")
    st.markdown("### Problem Statement: *'Silence reads as inaction.'*")
    st.info("The Goal: Reduce CS Slack/Email volume by 40% through self-serve visibility.")

    # 1. Dashboard View
    st.subheader("Organization Dashboard: Acme Corp")
    dashboard_data = {
        "Request ID": ["#RAY-9901", "#RAY-9854", "#RAY-9812", "#RAY-9799"],
        "Type": ["Laptop Order (20x)", "Software Access", "Wifi Repair", "New Hire Sync"],
        "Status": ["In Progress", "Resolved", "Acknowledged", "Closed"],
        "SLA Status": ["🟡 2h to Breach", "✅ Fulfilled", "🟢 On Track", "✅ Completed"],
        "Last Updated": ["2 hours ago", "1 day ago", "15 mins ago", "4 days ago"]
    }
    st.dataframe(pd.DataFrame(dashboard_data), use_container_width=True, hide_index=True)

    st.divider()

    # 2. Audit Trail / Timeline View
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.subheader("🔍 Detailed Audit Trail: #RAY-9901")
        st.write("**Request Description:** 20x MacBook Pro M3 for Engineering Team")
        
        # Timeline Logic
        timeline = [
            {"icon": "✅", "status": "Submitted", "time": "Oct 24, 09:00 AM", "note": "Client (Victor Anderson): 'Need these for the Nov 1st batch of new hires.'"},
            {"icon": "✅", "status": "Acknowledged", "time": "Oct 24, 09:15 AM", "note": "System: Assigned to Hardware Fulfillment team. SLA: 5 Business Days."},
            {"icon": "🔵", "status": "In Progress", "time": "Oct 24, 11:30 AM", "note": "Ops (Sarah): '15 units sourced. Awaiting 5 more from regional warehouse.'"},
            {"icon": "⚪", "status": "Resolved", "time": "Pending", "note": "-"},
        ]

        for event in timeline:
            with st.container():
                c1, c2 = st.columns([1, 15])
                c1.write(event["icon"])
                c2.markdown(f"**{event['status']}** | {event['time']}")
                c2.caption(event["note"])
                st.write("")

    with col_b:
        st.subheader("🛠️ Internal Rayda Ops View")
        st.caption("Internal-only context for CS and Ops teams.")
        with st.expander("Internal Notes (Hidden from Client)", expanded=True):
            st.warning("Supply chain issue: Regional warehouse delayed by 48hrs due to weather.")
            st.button("Post Internal Note")
        
        st.button("Update Status to Resolved", type="primary", use_container_width=True)
        st.button("Flag for CS Manager Review", use_container_width=True)

# ==========================================
# PAGE 2: AI STRATEGY (TASK 2)
# ==========================================
elif page == "📈 AI Strategy & Metrics (Task 2)":
    st.title("📈 Task 2: AI Measurement Framework")
    st.markdown("### Feature: AI-Powered IT Workflow Automation")

    # 1. Simulator Controls
    st.sidebar.subheader("Adjust AI Sensitivity")
    threshold = st.sidebar.slider("AI Confidence Threshold (%)", 50, 99, 85, 
                                  help="High threshold = AI is cautious. Low threshold = AI is aggressive.")
    
    # 2. Logic Simulation
    total_reqs = 1000
    np.random.seed(42)
    scores = np.random.normal(78, 12, total_reqs)
    
    automated_count = sum(scores > threshold)
    auto_rate = (automated_count / total_reqs)
    
    # Guardrail logic
    reopen_rate = max(1.5, (100 - threshold) * 0.38)

    # 3. Metrics (With New CSS Styling Applied)
    m1, m2, m3 = st.columns(3)
    m1.metric("North Star: Automation Rate", f"{auto_rate:.1%}")
    m2.metric("Guardrail: Re-open Rate", f"{reopen_rate:.1f}%", delta=f"{int(automated_count*(reopen_rate/100))} tickets", delta_color="inverse")
    
    if reopen_rate > 10:
        m3.error("Status: CRITICAL RISK")
    elif reopen_rate > 5:
        m3.warning("Status: CAUTION")
    else:
        m3.success("Status: HEALTHY")

    # 4. Chart
    st.divider()
    st.subheader("Scale vs. Trust Frontier")
    
    t_range = list(range(50, 100))
    chart_data = pd.DataFrame({
        "Threshold": t_range,
        "Automation %": [(len(scores[scores > t]) / total_reqs) * 100 for t in t_range],
        "Re-open Risk %": [(max(1.5, (100 - t) * 0.38)) for t in t_range]
    }).set_index("Threshold")
    
    st.line_chart(chart_data)
    
    st.markdown(f"""
    **Victor's Defense Strategy:**
    - This simulation helps us find the 'Sweet Spot' for our launch. 
    - At a **{threshold}% threshold**, our re-open rate is **{reopen_rate:.1f}%**.
    - If this moves into the **'Caution' or 'Critical'** zones, our system alerts the Ops Lead to manually override the AI until the model is retrained.
    """)
