import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(page_title="Victor Anderson | Rayda Assessment", layout="wide")

# --- CUSTOM CSS FOR TIMELINE ---
st.markdown("""
    <style>
    .reportview-container .main .block-container { padding-top: 2rem; }
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_index=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Assessment Navigation")
page = st.sidebar.radio("Select Task Demo:", ["🖥️ Client Trust Portal (Task 1)", "📈 AI Strategy & Metrics (Task 2)"])

st.sidebar.divider()
st.sidebar.markdown(f"**Current View:** {page}")

# ==========================================
# PAGE 1: CLIENT TRUST PORTAL (TASK 1)
# ==========================================
if page == "🖥️ Client Trust Portal (Task 1)":
    st.title("🖥️ Task 1: Enterprise Request Tracking")
    st.info("Problem: Clients have no visibility. Solution: Real-time status tracking & audit trails.")

    # 1. Dashboard View
    st.subheader("Organization Dashboard: Acme Corp")
    data = {
        "Request ID": ["#RAY-9901", "#RAY-9854", "#RAY-9812", "#RAY-9799"],
        "Type": ["Laptop Order (20x)", "Software Access", "Wifi Hardware Repair", "New Hire Provisioning"],
        "Status": ["In Progress", "Resolved", "Acknowledged", "Closed"],
        "SLA Status": ["🟡 2h to Breached", "✅ Fulfilled", "🟢 On Track", "✅ Completed"],
        "Last Updated": ["2 hours ago", "1 day ago", "15 mins ago", "4 days ago"]
    }
    df = pd.DataFrame(data)
    
    # Styled table
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.divider()

    # 2. Audit Trail / Timeline View
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.subheader("🔍 Detailed Audit Trail: #RAY-9901")
        st.write("**Request:** 20x MacBook Pro M3 for Engineering Team")
        
        # Timeline Logic
        timeline = [
            {"icon": "✅", "status": "Submitted", "time": "Oct 24, 09:00 AM", "note": "Client (Victor Anderson): 'Need these for the Nov 1st batch of new hires.'"},
            {"icon": "✅", "status": "Acknowledged", "time": "Oct 24, 09:15 AM", "note": "System: Assigned to Hardware Fulfillment team. SLA confirmed (5 Days)."},
            {"icon": "🔵", "status": "In Progress", "time": "Oct 24, 11:30 AM", "note": "Ops (Sarah): '15 units sourced. Awaiting 5 more from regional warehouse.'"},
            {"icon": "⚪", "status": "Resolved", "time": "Pending", "note": "-"},
            {"icon": "⚪", "status": "Closed", "time": "Pending", "note": "-"}
        ]

        for event in timeline:
            with st.container():
                c1, c2 = st.columns([1, 15])
                c1.write(event["icon"])
                c2.markdown(f"**{event['status']}** | {event['time']}")
                c2.caption(event["note"])
                st.write("")

    with col_b:
        st.subheader("🛠️ Internal Ops Actions")
        st.caption("This section is only visible to Rayda Employees.")
        with st.expander("Add Internal Note (Hidden from Client)", expanded=True):
            st.text_area("Note content...", placeholder="e.g., Shipping carrier delayed due to weather.")
            st.checkbox("Mark as Urgent")
            st.button("Post Internal Note")
        
        st.button("Update Status: Resolved", use_container_width=True)
        st.error("Flag SLA Breach")

# ==========================================
# PAGE 2: AI STRATEGY (TASK 2)
# ==========================================
elif page == "📈 AI Strategy & Metrics (Task 2)":
    st.title("📈 Task 2: AI Measurement Framework")
    st.markdown("### Feature: AI-Powered IT Request Automation")

    # 1. Simulator Controls
    st.sidebar.subheader("Adjust AI Parameters")
    threshold = st.sidebar.slider("AI Confidence Threshold (%)", 50, 99, 85, 
                                  help="The minimum confidence the AI needs to take action without a human.")
    
    # 2. Simulation Brain
    total_requests = 1000
    np.random.seed(42)
    scores = np.random.normal(78, 12, total_requests)
    
    # Logic: High threshold = lower volume, but lower error (re-open) rate.
    automated_count = sum(scores > threshold)
    automation_rate = (automated_count / total_requests)
    
    # Re-open rate (Guardrail) logic
    # As threshold goes down, error rate goes up exponentially
    base_error = 1.2
    risk_multiplier = (100 - threshold) * 0.35
    reopen_rate = base_error + risk_multiplier

    # 3. Metrics Display
    m1, m2, m3 = st.columns(3)
    m1.metric("North Star: Automation Rate", f"{automation_rate:.1%}", help="Target: 30% by Day 90")
    m2.metric("Guardrail: Re-open Rate", f"{reopen_rate:.1f}%", 
              delta=f"{int(automated_count * (reopen_rate/100))} tickets", delta_color="inverse")
    
    status = "✅ HEALTHY" if reopen_rate < 5 else "🟡 AT RISK" if reopen_rate < 10 else "🚨 CRITICAL"
    m3.metric("System Health", status)

    # 4. Visualizing the Decision Frontier
    st.divider()
    st.subheader("The Trade-off: Scale vs. Trust")
    
    # Generate data for the line chart
    t_range = list(range(50, 100))
    chart_data = pd.DataFrame({
        "Threshold": t_range,
        "Automation %": [(len(scores[scores > t]) / total_requests) * 100 for t in t_range],
        "Risk (Re-open Rate)": [(base_error + (100 - t) * 0.35) for t in t_range]
    }).set_index("Threshold")
    
    st.line_chart(chart_data)
    
    st.write("**Victor's Strategic Insight:**")
    st.write(f"At a **{threshold}% threshold**, we automate **{automated_count}** requests. To reach our 30% North Star target, we need to balance the AI's aggressiveness with our re-open guardrail. If we go below 75% confidence, we breach our 10% re-open safety limit.")
