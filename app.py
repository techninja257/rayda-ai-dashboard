import streamlit as st
import pandas as pd
import datetime

# --- CONFIG ---
st.set_page_config(page_title="Victor's Rayda Assessment Demo", layout="wide")

# --- NAVIGATION ---
page = st.sidebar.radio("Go to:", ["📈 AI Strategy (Task 2)", "🖥️ Client Trust Portal (Task 1)"])

# ==========================================
# PAGE 1: AI STRATEGY (TASK 2) - THE PREVIOUS APP
# ==========================================
if page == "📈 AI Strategy (Task 2)":
    st.title("🛡️ AI Confidence vs. Guardrail Simulator")
    st.info("Goal: Demonstrate how we scale automation without breaking client trust.")
    
    threshold = st.sidebar.slider("AI Confidence Threshold (%)", 50, 99, 85)
    
    col1, col2, col3 = st.columns(3)
    # (Keeping your existing logic simplified for space)
    auto_rate = (100 - threshold) * 1.2
    error_rate = max(1.5, (100 - threshold) * 0.4)
    
    col1.metric("Automation Rate", f"{auto_rate:.1f}%")
    col2.metric("Re-open Rate (Guardrail)", f"{error_rate:.1f}%", delta_color="inverse")
    col3.success("System Status: Healthy") if error_rate < 5 else col3.warning("System Status: At Risk")
    st.line_chart({"Automation": [auto_rate], "Risk": [error_rate]})

# ==========================================
# PAGE 2: CLIENT TRUST PORTAL (TASK 1)
# ==========================================
else:
    st.title("🖥️ Enterprise Admin: Request Tracking")
    st.markdown("### Active Requests for *Acme Corp*")

    # Mock Data for the Dashboard
    data = {
        "Request ID": ["#RAY-9901", "#RAY-9854", "#RAY-9812"],
        "Type": ["Laptop Order (20x)", "Software Access", "Wifi Hardware Repair"],
        "Status": ["In Progress", "Resolved", "Acknowledged"],
        "SLA Status": ["🟢 On Track", "✅ Fulfilled", "🟡 1h Left"],
        "Last Updated": ["2 hours ago", "1 day ago", "10 mins ago"]
    }
    df = pd.DataFrame(data)
    st.table(df)

    st.write("---")
    st.subheader("🔍 Deep Dive: Request #RAY-9901")
    
    # The Timeline - This is the "Audit Trail" from your PRD
    st.markdown("#### **Status Timeline**")
    
    # Use columns to simulate a timeline
    events = [
        ("✅", "Submitted", "Oct 24, 09:00 AM", "Client: Victor Anderson"),
        ("✅", "Acknowledged", "Oct 24, 09:15 AM", "System: Auto-assigned to Hardware Team"),
        ("🔵", "In Progress", "Oct 24, 11:30 AM", "Ops: 'Sourcing 15/20 laptops from local warehouse.'"),
        ("⚪", "Resolved", "Pending", "-"),
        ("⚪", "Closed", "Pending", "-")
    ]
    
    for icon, status, time, note in events:
        col_icon, col_txt = st.columns([1, 15])
        with col_icon:
            st.write(icon)
        with col_txt:
            st.markdown(f"**{status}** | {time}")
            st.caption(note)

    # Demoing the "Internal Note" feature vs "Client Note"
    with st.expander("🛠️ View Internal Rayda Ops View (Hidden from Client)"):
        st.warning("INTERNAL ONLY: Supply chain delay on remaining 5 units. Expected arrival Oct 28.")
        st.button("Add Internal Note")
        st.button("Update Status to Resolved")

    st.sidebar.markdown("---")
    st.sidebar.write("**Victor's Demo Notes:**")
    st.sidebar.info("This view solves the 'Silence = Inaction' problem by providing a real-time audit trail and differentiating between internal/external notes.")
