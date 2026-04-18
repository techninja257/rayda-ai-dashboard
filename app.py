import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(page_title="Victor Anderson | Rayda Assessment", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    [data-testid="stMetric"] {
        background-color: #000000 !important;
        padding: 20px !important;
        border-radius: 12px !important;
        border: 1px solid #333333 !important;
        color: white !important;
    }
    [data-testid="stMetricLabel"] > div { color: #FFFFFF !important; font-weight: bold !important; }
    [data-testid="stMetricValue"] > div { color: #FFFFFF !important; }
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
            {"icon": "✅", "status": "Submitted", "time": "Oct 24, 09:00 AM", "note": "Client (Victor Anderson): 'Need these for the Nov 1st batch.'"},
            {"icon": "✅", "status": "Acknowledged", "time": "Oct 24, 09:15 AM", "note": "System: Assigned to Hardware team. SLA: 5 Days."},
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
    threshold = st.sidebar.slider("AI Confidence Threshold (%)", 50, 99, 85)
    
    total_reqs = 1000
    np.random.seed(42)
    scores = np.random.normal(78, 12, total_reqs)
    automated_count = sum(scores > threshold)
    auto_rate = (automated_count / total_reqs)
    reopen_rate = max(1.5, (100 - threshold) * 0.38)

    m1, m2, m3 = st.columns(3)
    m1.metric("North Star: Automation Rate", f"{auto_rate:.1%}")
    m2.metric("Guardrail: Re-open Rate", f"{reopen_rate:.1f}%", delta=f"{int(automated_count*(reopen_rate/100))} tickets", delta_color="inverse")
    m3.success("Status: HEALTHY") if reopen_rate < 5 else m3.warning("Status: CAUTION") if reopen_rate < 10 else m3.error("Status: CRITICAL")

    st.divider()
    st.subheader("The Trade-off: Scale vs. Trust")
    t_range = list(range(50, 100))
    chart_data = pd.DataFrame({
        "Threshold": t_range,
        "Automation %": [(len(scores[scores > t]) / total_reqs) * 100 for t in t_range],
        "Re-open Risk %": [(max(1.5, (100 - t) * 0.38)) for t in t_range]
    }).set_index("Threshold")
    st.line_chart(chart_data)

# ==========================================
# PAGE 3: SPRINT RECOVERY (TASK 3)
# ==========================================
else:
    st.title("🚑 Task 3: Sprint Forensic & Recovery")
    st.markdown("### Diagnosis: 40% of planned tickets did not ship.")
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.subheader("📊 Post-Mortem Analysis")
        st.write("Root Cause: **Scope Creep** and **Vague Definition of Ready (DoR)**.")
        chart_miss = pd.DataFrame({"Status": ["Shipped", "Missed (Scope Creep)"], "Value": [60, 40]})
        st.bar_chart(chart_miss.set_index("Status"))

    with col_c2:
        st.subheader("🛡️ The 'Scope-Swap' Calculator")
        st.info("Mid-sprint requests must follow a zero-sum rule.")
        new_task_weight = st.number_input("Weight of new request (Points):", 1, 13, 5)
        st.warning(f"To add this, you MUST remove at least {new_task_weight} points from the current sprint.")
        swap_item = st.text_input("Item to be removed from Sprint:", "e.g., Update Profile UI")
        if st.button("Authorize Scope Swap"):
            st.success(f"Swap Logged: Added {new_task_weight}pts, Removed '{swap_item}'")

    st.divider()
    st.subheader("📝 New Structural Artifacts")
    tab_dor, tab_dod = st.tabs(["Definition of Ready (DoR)", "Definition of Done (DoD)"])
    
    with tab_dor:
        st.markdown("""
        - [ ] **Technical Handshake:** Dev confirms AC is understood.
        - [ ] **Scope Boundary:** Ticket explicitly states what is NOT being done.
        - [ ] **Design Lock:** Figma mocks include all edge cases (error/loading).
        """)
        
    with tab_dod:
        st.markdown("""
        - [ ] **Scope Integrity:** No 'while-you-are-at-it' scope added.
        - [ ] **Verification:** Verified in Staging against original AC.
        - [ ] **Analytics:** Event tracking verified (Amplitude/PostHog).
        """)
