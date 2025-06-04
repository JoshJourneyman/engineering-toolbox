
import streamlit as st

st.set_page_config(page_title="Engineering Toolbox", layout="centered")

st.title("🧰 Engineering Toolbox")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Feedrate & MRR",
    "Unit Converter",
    "Tap Drill Chart",
    "Surface Speed/Feed",
    "Bolt Torque"
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
