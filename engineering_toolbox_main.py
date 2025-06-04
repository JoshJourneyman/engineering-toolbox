
import streamlit as st
import math

st.set_page_config(page_title="Engineering Toolbox", layout="centered")
st.title("🧰 Engineering Toolbox (Complete)")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "Feedrate & MRR",
    "Unit Converter",
    "Tap Drill Chart",
    "Surface Speed/Feed",
    "Bolt Torque",
    "Thread Engagement",
    "Hole Tolerance",
    "Production Estimator",
    "Takt Time"
])

# --- Tab 1: Feedrate & MRR ---
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

# --- Tab 2: Unit Converter ---
with tab2:
    st.header("Millimeter ↔ Inch Converter")
    conversion_type = st.selectbox("Select conversion type:", ["Millimeters to Inches", "Inches to Millimeters"])
    value = st.number_input("Enter value:", min_value=0.0, step=0.01, format="%.4f")
    if conversion_type == "Millimeters to Inches":
        result = value / 25.4
        st.write(f"**{value:.4f} mm** is **{result:.4f} in**")
    else:
        result = value * 25.4
        st.write(f"**{value:.4f} in** is **{result:.4f} mm**")

# --- Tab 3: Tap Drill Chart ---
with tab3:
    st.header("Tap Drill Chart")
    system = st.selectbox("Thread System", ["Inch (UNC/UNF)", "Metric"])
    if system == "Inch (UNC/UNF)":
        thread = st.selectbox("Select Thread", [
            "1/4-20 UNC", "1/4-28 UNF", "5/16-18 UNC", "3/8-16 UNC", "3/8-24 UNF",
            "7/16-14 UNC", "1/2-13 UNC", "9/16-12 UNC", "5/8-11 UNC", "3/4-10 UNC",
            "7/8-9 UNC", "1-8 UNC"
        ])
        inch_chart = {
            "1/4-20 UNC": "0.201 in (#7 drill)",
            "1/4-28 UNF": "0.213 in (#3 drill)",
            "5/16-18 UNC": "0.257 in (F drill)",
            "3/8-16 UNC": "0.313 in (5/16 drill)",
            "3/8-24 UNF": "0.332 in (Q drill)",
            "7/16-14 UNC": "0.368 in (U drill)",
            "1/2-13 UNC": "0.421 in (27/64 drill)",
            "9/16-12 UNC": "0.484 in (31/64 drill)",
            "5/8-11 UNC": "0.531 in (17/32 drill)",
            "3/4-10 UNC": "0.656 in (21/32 drill)",
            "7/8-9 UNC": "0.781 in (25/32 drill)",
            "1-8 UNC": "0.906 in (29/32 drill)"
        }
        st.write(f"Recommended Tap Drill: **{inch_chart[thread]}**")
    else:
        thread = st.selectbox("Select Thread", [
            "M3x0.5", "M4x0.7", "M5x0.8", "M6x1.0", "M8x1.25", "M10x1.5", "M12x1.75", "M16x2.0", "M20x2.5"
        ])
        metric_chart = {
            "M3x0.5": "2.5 mm",
            "M4x0.7": "3.3 mm",
            "M5x0.8": "4.2 mm",
            "M6x1.0": "5.0 mm",
            "M8x1.25": "6.8 mm",
            "M10x1.5": "8.5 mm",
            "M12x1.75": "10.2 mm",
            "M16x2.0": "14.0 mm",
            "M20x2.5": "17.5 mm"
        }
        st.write(f"Recommended Tap Drill: **{metric_chart[thread]}**")

# --- Tab 4: Surface Speed / Feed Calculator ---
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

# --- Tab 5: Bolt Torque Calculator ---
with tab5:
    st.header("Bolt Torque Calculator (Machinery's Handbook)")
    units = st.selectbox("Torque Units", ["ft-lb", "in-lb", "Nm"])
    system = st.selectbox("Bolt System", ["Inch", "Metric"])
    condition = st.radio("Thread Condition", ["Dry", "Lubed"])

    if system == "Inch":
        bolt = st.selectbox("Bolt Size (Grade 5)", [
            "1/4-20", "5/16-18", "3/8-16", "7/16-14", "1/2-13", "9/16-12", "5/8-11", "3/4-10"
        ])
        torque_ft_lb = {
            "1/4-20": 8,
            "5/16-18": 17,
            "3/8-16": 31,
            "7/16-14": 50,
            "1/2-13": 75,
            "9/16-12": 110,
            "5/8-11": 150,
            "3/4-10": 270
        }
        factor = 1.0 if condition == "Dry" else 0.75
        ft_lb = torque_ft_lb[bolt] * factor
    else:
        bolt = st.selectbox("Bolt Size (Grade 10.9)", [
            "M6", "M8", "M10", "M12", "M14", "M16", "M18", "M20"
        ])
        torque_nm = {
            "M6": 11,
            "M8": 27,
            "M10": 54,
            "M12": 95,
            "M14": 150,
            "M16": 240,
            "M18": 330,
            "M20": 460
        }
        factor = 1.0 if condition == "Dry" else 0.75
        ft_lb = torque_nm[bolt] * factor * 0.7376

    if units == "ft-lb":
        output = ft_lb
        label = "ft-lb"
    elif units == "in-lb":
        output = ft_lb * 12
        label = "in-lb"
    else:
        output = ft_lb / 0.7376
        label = "Nm"

    st.write(f"Recommended Torque: **{output:.1f} {label}**")

# --- Tab 6: Thread Engagement ---
with tab6:
    st.header("Thread Engagement Calculator")
    depth = st.number_input("Threaded Hole Depth (in)", min_value=0.01)
    pitch = st.number_input("Thread Pitch (in)", min_value=0.001)
    if st.button("Calculate Engagement"):
        threads_engaged = depth / pitch
        percent_engagement = min((threads_engaged / 6) * 100, 100)
        st.write(f"**Threads Engaged:** {threads_engaged:.1f}")
        st.write(f"**Estimated % Engagement:** {percent_engagement:.1f}%")

# --- Tab 7: Hole Tolerance ---
with tab7:
    st.header("Hole Tolerance Checker")
    nominal = st.number_input("Nominal Hole Size (in)", min_value=0.01)
    clearance = st.number_input("Clearance (in)", value=0.002)
    min_dia = nominal
    max_dia = nominal + clearance
    st.write(f"Min Hole Size: **{min_dia:.4f} in**")
    st.write(f"Max Hole Size: **{max_dia:.4f} in**")

# --- Tab 8: Production Rate Estimator ---
with tab8:
    st.header("Production Rate Estimator")
    cycle_time_hr = st.number_input("Cycle Time per Part (hours)", min_value=0.01, step=0.01, format="%.2f")
    shift_hours = st.number_input("Shift Length (hours)", min_value=1.0, step=0.5)
    breaks_min = st.number_input("Break Time (minutes)", min_value=0.0, step=5.0)
    if st.button("Estimate Production"):
        available_hours = shift_hours - (breaks_min / 60)
        parts_per_day = available_hours / cycle_time_hr
        st.subheader("Estimated Output")
        st.write(f"Available Time: {available_hours:.2f} hours")
        st.write(f"Estimated Parts per Day: {parts_per_day:.0f}")

# --- Tab 9: Takt Time Calculator ---
with tab9:
    st.header("Takt Time Calculator")
    demand = st.number_input("Customer Demand (units/day)", min_value=1)
    available_time = st.number_input("Available Work Time (minutes/day)", min_value=1.0)
    if st.button("Calculate Takt Time"):
        takt_time = available_time / demand
        st.subheader(f"Takt Time: {takt_time:.2f} min/unit")
        if takt_time < 1:
            st.warning("⚠️ Your takt time is less than 1 min/unit. Ensure machines can keep up.")
