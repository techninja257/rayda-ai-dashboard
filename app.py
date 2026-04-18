import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(page_title="Victor Anderson | Rayda Assessment", layout="wide")

# --- CUSTOM CSS (BLACK CARDS, WHITE TEXT) ---
st.markdown("""
    <style>
    [data-testid="stMetric"] {
        background-color: #000000 !important;
        padding: 20px !important;
        border-radius: 12px !important;
        border: 1px solid #333333 !important;
    }
    [data-testid="stMetricLabel"] > div { color: #FFFFFF !important; font-weight: bold !important; }
    [data-testid="stMetricValue"] > div { color: #FFFFFF !important; }
    [data-testid="stMetricDelta"] > div { color: #FF4B4B !important; }
    .main .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Victor Anderson: PM Assessment")
page = st.sidebar.radio("Select Task Demo:", [
    "🖥️ Client Trust Portal (Task 1)", 
    "📈 AI Strategy & Metrics (Task 2)",
    "🚑 Sprint Recovery Dashboard (Task 3)"
])

st.sidebar.divider()
st.sidebar.info("Demoing: Craft, Measurement, and Systems Thinking.")

# ==========================================
# PAGE 1: CLIENT TRUST PORTAL (TASK 1)
# ==========================================
if page == "🖥️ Client Trust Portal (Task 1)":
    st.title("🖥️ Task 1: Enterprise Request Tracking")
    st.info("Goal: Provide 24/7 visibility to reduce CS overhead and build client trust.")

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
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.subheader("🔍 Detailed Audit Trail: #RAY-9901")
        timeline = [
            {"icon": "✅", "status": "Submitted", "time": "Oct 24, 09:00 AM", "note": "Client: 'Need these for the Nov 1st batch.'"},
            {"icon": "✅", "status": "Acknowledged", "time": "Oct 24, 09:15 AM", "note": "System: Assigned to Hardware team."},
            {"icon": "🔵", "status": "In Progress", "time": "Oct 24, 11:30 AM", "note": "Ops (Sarah): '15 units sourced. Awaiting 5 more.'"},
            {"icon": "⚪", "status": "Resolved", "time": "Pending", "note": "-"},
        ]
        for event in timeline:
            c1, c2 = st.columns([1, 15])
            c1.write(event["icon"])
            c2.markdown(f"**{event['status']}** | {event['time']}")
            c2.caption(event["note"])
    with col_b:
        st.subheader("🛠️ Internal Ops View")
        with st.expander("Internal Notes", expanded=True):
            st.warning("Regional warehouse delay (48hrs).")
            st.button("Post Internal Note")
        st.button("Update Status to Resolved", type="primary", use_container_width=True)

# ==========================================
# PAGE 2: AI STRATEGY (TASK 2)
# ==========================================
elif page == "📈 AI Strategy & Metrics (Task 2)":
    st.title("📈 Task 2: AI Measurement Framework")
    
    # 1. Sidebar Control
    st.sidebar.subheader("Adjust AI Sensitivity")
    threshold = st.sidebar.slider("AI Confidence Threshold (%)", 50, 99, 85)
    
    # 2. Simulation Brain
    np.random.seed(42)
    scores = np.random.normal(78, 12, 1000)
    
    current_auto_count = sum(scores > threshold)
    current_auto_rate = current_auto_count / 1000
    current_reopen_rate = max(1.5, (100 - threshold) * 0.38)

    # 3. Metrics (Black cards, White text)
    m1, m2, m3 = st.columns(3)
    m1.metric("Automation Rate", f"{current_auto_rate:.1%}")
    m2.metric("Re-open Rate (Risk)", f"{current_reopen_rate:.1f}%", delta=f"{int(current_auto_count*(current_reopen_rate/100))} tickets", delta_color="inverse")
    
    if current_reopen_rate > 10:
        m3.error("Status: CRITICAL")
    elif current_reopen_rate > 5:
        m3.warning("Status: AT RISK")
    else:
        m3.success("Status: HEALTHY")

    st.divider()
    st.subheader("Scale vs. Trust Frontier")
    
    # 4. Corrected Chart Logic
    t_range = np.arange(50, 100, 1)
    auto_points = [(sum(scores > t) / 1000) * 100 for t in t_range]
    risk_points = [max(1.5, (100 - t) * 0.38) for t in t_range]
    
    chart_df = pd.DataFrame({
        "Confidence_Threshold": t_range,
        "Automation_Rate": auto_points,
        "Reopen_Risk": risk_points
    }).set_index("Confidence_Threshold")
    
    st.line_chart(chart_df)
    
    st.markdown(f"""
    **Strategic Takeaway:** 
    At a **{threshold}% threshold**, we find the balance between hitting our North Star and protecting client trust. 
    Notice how as you lower the threshold to increase volume, the risk line rises sharply.
    """)

# ==========================================
# PAGE 3: SPRINT RECOVERY (TASK 3)
# ==========================================
else:
    st.title("🚑 Task 3: Sprint Forensic & Recovery")
    st.markdown("### Diagnosis: 40% of planned tickets did not ship.")
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.subheader("📊 Post-Mortem Analysis")
        chart_miss = pd.DataFrame({
            "Category": ["Shipped", "Missed (Scope Creep)", "Missed (Vague AC)"],
            "Points": [60, 25, 15]
        }).set_index("Category")
        st.bar_chart(chart_miss)

    with col_c2:
        st.subheader("🛡️ The 'Scope-Swap' Calculator")
        st.info("Mid-sprint requests require a zero-sum trade-off.")
        weight = st.number_input("New Task Points:", 1, 13, 5)
        st.warning(f"Required: Remove {weight} points from current sprint.")
        swap = st.text_input("Swap with:", "e.g., UI Refactor")
        if st.button("Authorize Scope Swap"):
            st.success(f"Swap Logged: Added {weight}pts, Removed '{swap}'")

    st.divider()
    st.subheader("📝 New Structural Artifacts")
    tab1, tab2 = st.tabs(["Definition of Ready (DoR)", "Definition of Done (DoD)"])
    with tab1:
        st.markdown("- [ ] **Technical Handshake:** Assigned dev confirms AC is clear.\n- [ ] **Scope Boundary:** Explicitly states what is NOT being built.\n- [ ] **Design Lock:** All edge cases mocked.")
    with tab2:
        st.markdown("- [ ] **Scope Integrity:** No unauthorized scope added.\n- [ ] **Verification:** Passed in Staging.\n- [ ] **Analytics:** Event tracking verified.")
