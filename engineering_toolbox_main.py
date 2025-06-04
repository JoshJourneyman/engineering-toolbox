
import streamlit as st
import math

st.set_page_config(page_title="Engineering Toolbox", layout="centered")
st.title("🧰 Engineering Toolbox (Main Tools)")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Feedrate & MRR",
    "Unit Converter",
    "Tap Drill Chart",
    "Surface Speed/Feed",
    "Bolt Torque",
    "Thread Engagement",
    "Hole Tolerance"
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
    thread = st.selectbox("Thread Size", ["1/4-20 UNC", "5/16-18 UNC", "3/8-16 UNC", "M6x1.0", "M8x1.25"])
    drill_chart = {
        "1/4-20 UNC": "0.201 in",
        "5/16-18 UNC": "0.257 in",
        "3/8-16 UNC": "0.313 in",
        "M6x1.0": "5.0 mm",
        "M8x1.25": "6.8 mm"
    }
    st.write(f"Recommended Tap Drill Size: **{drill_chart[thread]}**")

with tab4:
    st.header("Surface Speed / Feed Calculator")
    diameter = st.number_input("Tool Diameter (in)", min_value=0.01, step=0.01)
    sfm = st.number_input("Surface Feet per Minute (SFM)", min_value=10)
    ipt = st.number_input("Feed per Tooth (IPT)", min_value=0.001, step=0.001, format="%.3f")
    flutes_sf = st.number_input("Number of Flutes", min_value=1, step=1)
    if st.button("Calculate RPM & IPM"):
        rpm_calc = (sfm * 3.82) / diameter
        ipm = rpm_calc * ipt * flutes_sf
        st.subheader("Results")
        st.write(f"**RPM:** {rpm_calc:.0f}")
        st.write(f"**Feedrate:** {ipm:.2f} IPM")

with tab5:
    st.header("Bolt Torque Calculator")
    bolt_size = st.selectbox("Bolt Size", ["1/4-20", "5/16-18", "3/8-16", "M6", "M8"])
    dry_torque = {
        "1/4-20": 8,
        "5/16-18": 17,
        "3/8-16": 30,
        "M6": 7,
        "M8": 17
    }
    lubed_torque = {
        "1/4-20": 6,
        "5/16-18": 13,
        "3/8-16": 23,
        "M6": 5,
        "M8": 13
    }
    st.write(f"Dry Torque: **{dry_torque[bolt_size]} ft-lbs**")
    st.write(f"Lubed Torque: **{lubed_torque[bolt_size]} ft-lbs**")

with tab6:
    st.header("Thread Engagement Calculator")
    depth = st.number_input("Threaded Hole Depth (in)", min_value=0.01)
    pitch = st.number_input("Thread Pitch (in)", min_value=0.001)
    if st.button("Calculate Engagement"):
        threads_engaged = depth / pitch
        percent_engagement = min((threads_engaged / 6) * 100, 100)
        st.write(f"**Threads Engaged:** {threads_engaged:.1f}")
        st.write(f"**Estimated % Engagement:** {percent_engagement:.1f}%")

with tab7:
    st.header("Hole Tolerance Checker")
    nominal = st.number_input("Nominal Hole Size (in)", min_value=0.01)
    clearance = st.number_input("Clearance (in)", value=0.002)
    min_dia = nominal
    max_dia = nominal + clearance
    st.write(f"Min Hole Size: **{min_dia:.4f} in**")
    st.write(f"Max Hole Size: **{max_dia:.4f} in**")
    st.caption("This represents a loose clearance fit. Adjust clearance for tighter or interference fits.")
