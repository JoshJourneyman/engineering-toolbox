
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Engineering Toolbox", layout="centered")
st.title("🧰 Engineering Toolbox")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Feedrate & MRR",
    "Unit Converter",
    "Tap Drill Chart",
    "Surface Speed/Feed",
    "Bolt Torque",
    "Production Estimator",
    "G-code Viewer",
    "Takt Time"
])

with tab1:
    st.header("Feedrate & MRR Calculator")
    rpm = st.number_input("Spindle Speed (RPM)", min_value=100, max_value=12000, step=10)
    fpt = st.number_input("Feed per Tooth (in)", min_value=0.001, max_value=0.05, step=0.001, format="%.3f")
    flutes = st.number_input("Number of Flutes", min_value=1, max_value=10, step=1)
    width = st.number_input("Width of Cut (in)", min_value=0.01, max_value=5.0, step=0.01)
    depth = st.number_input("Depth of Cut (in)", min_value=0.01, max_value=1.0, step=0.01)
    if st.button("Calculate Feedrate & MRR"):
        feedrate = rpm * fpt * flutes
        mrr = width * depth * feedrate
        st.subheader("Results")
        st.write(f"**Feedrate:** {feedrate:.2f} IPM")
        st.write(f"**Material Removal Rate:** {mrr:.2f} in³/min")

with tab2:
    st.header("Millimeter ↔ Inch Converter")
    conversion_type = st.selectbox("Select conversion type:", ["Millimeters to Inches", "Inches to Millimeters"])
    value = st.number_input("Enter value:", min_value=0.0, step=0.01, format="%.4f")
    if conversion_type == "Millimeters to Inches":
        result = value / 25.4
        st.write(f"**{value:.4f} mm** is **{result:.4f} in**")
        st.caption("Formula: inches = mm / 25.4")
    else:
        result = value * 25.4
        st.write(f"**{value:.4f} in** is **{result:.4f} mm**")
        st.caption("Formula: mm = inches × 25.4")

with tab3:
    st.header("Tap Drill Chart")
    st.write("🚧 Tap Drill Chart Tool – Coming Soon!")

with tab4:
    st.header("Surface Speed / Feed Calculator")
    st.write("🚧 Surface Speed & Feed Rate Tool – Coming Soon!")

with tab5:
    st.header("Bolt Torque Calculator")
    st.write("🚧 Bolt Torque Lookup Tool – Coming Soon!")

with tab6:
    st.header("Production Rate Estimator")
    cycle_time = st.number_input("Cycle Time per Part (minutes)", min_value=0.01, step=0.01)
    shift_hours = st.number_input("Shift Length (hours)", min_value=1.0, step=0.5)
    breaks = st.number_input("Break Time (minutes)", min_value=0.0, step=5.0)
    if st.button("Estimate Production"):
        net_minutes = (shift_hours * 60) - breaks
        parts_per_day = net_minutes / cycle_time
        st.subheader("Estimated Output")
        st.write(f"Available Time: {net_minutes:.1f} minutes")
        st.write(f"Estimated Parts per Day: {parts_per_day:.0f}")

with tab7:
    st.header("G-code Viewer")
    uploaded_file = st.file_uploader("Upload G-code file (.nc or .txt)", type=["nc", "txt"])
    if uploaded_file:
        code_lines = uploaded_file.read().decode("utf-8").splitlines()
        st.text_area("G-code Preview", value="\n".join(code_lines[:50]), height=300)
        if st.checkbox("Show Tool Changes"):
            tool_lines = [line for line in code_lines if "T" in line and "M6" in line]
            st.write("Detected Tool Changes:")
            for tl in tool_lines:
                st.code(tl)

with tab8:
    st.header("Takt Time Calculator")
    demand = st.number_input("Customer Demand (units/day)", min_value=1)
    available_time = st.number_input("Available Work Time (minutes/day)", min_value=1.0)
    if st.button("Calculate Takt Time"):
        takt_time = available_time / demand
        st.subheader(f"Takt Time: {takt_time:.2f} min/unit")
        if takt_time < 1:
            st.warning("⚠️ Your takt time is less than 1 min/unit. Ensure machines can keep up.")
