import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Dynamic Pricing Strategy Simulator",
    page_icon="🚕",
    layout="centered"
)

st.title("🚕 Dynamic Pricing Strategy Simulator")
st.write("Real-time ride pricing based on demand, supply, and ride conditions.")

# =====================================================
# LOAD MODEL
# =====================================================
@st.cache_resource
def load_model():
    return joblib.load("model/dp_price_model.pkl")

model = load_model()

# =====================================================
# USER INPUTS
# =====================================================
st.header("🔧 Ride Parameters")

col1, col2 = st.columns(2)

with col1:
    riders = st.number_input("Number of Riders", min_value=1, value=50)
    drivers = st.number_input("Number of Drivers", min_value=1, value=25)
    location = st.selectbox("Location Category", ["Urban", "Suburban", "Rural"])
    loyalty = st.selectbox("Customer Loyalty Status", ["Regular", "Silver", "Gold"])

with col2:
    past_rides = st.number_input("Number of Past Rides", min_value=0, value=20)
    rating = st.slider("Average Rating", 1.0, 5.0, 4.2)
    time = st.selectbox("Time of Booking", ["Morning", "Afternoon", "Evening", "Night"])
    vehicle = st.selectbox("Vehicle Type", ["Economy", "Premium"])

duration = st.slider("Expected Ride Duration (minutes)", 5, 180, 45)

# =====================================================
# ENCODING MAPS
# =====================================================
location_map = {"Urban": 2, "Suburban": 1, "Rural": 0}
loyalty_map = {"Regular": 0, "Silver": 1, "Gold": 2}
time_map = {"Morning": 2, "Afternoon": 0, "Evening": 1, "Night": 3}
vehicle_map = {"Economy": 0, "Premium": 1}

# =====================================================
# FEATURE ENGINEERING
# =====================================================
demand_supply_ratio = riders / drivers
peak_time = 1 if time in ["Evening", "Night"] else 0

input_df = pd.DataFrame([{
    "Number_of_Riders": riders,
    "Number_of_Drivers": drivers,
    "Location_Category": location_map[location],
    "Customer_Loyalty_Status": loyalty_map[loyalty],
    "Number_of_Past_Rides": past_rides,
    "Average_Ratings": rating,
    "Time_of_Booking": time_map[time],
    "Vehicle_Type": vehicle_map[vehicle],
    "Expected_Ride_Duration": duration,
    "Demand_Supply_Ratio": demand_supply_ratio,
    "Peak_Time": peak_time
}])

# =====================================================
# SURGE MULTIPLIER LOGIC
# =====================================================
def get_surge_multiplier(ratio):
    if ratio < 1:
        return 1.0, "🟢 No Surge"
    elif ratio < 1.5:
        return 1.2, "🟡 Mild Surge"
    elif ratio < 2:
        return 1.5, "🟠 High Surge"
    else:
        return 2.0, "🔴 Extreme Surge"

surge_multiplier, surge_label = get_surge_multiplier(demand_supply_ratio)

# =====================================================
# PREDICTION
# =====================================================
if st.button("💰 Predict Ride Price"):
    predicted_price = model.predict(input_df)[0]
    base_price = predicted_price / surge_multiplier

    st.subheader("📊 Pricing Result")

    col1, col2 = st.columns(2)
    col1.metric("Base Price (₹)", f"₹{base_price:.2f}")
    col2.metric("Final Price (₹)", f"₹{predicted_price:.2f}")

    st.write("**Surge Level:**", surge_label)
    st.write(f"**Surge Multiplier:** ×{surge_multiplier}")

    # =====================================================
    # PRICE COMPARISON CHART
    # =====================================================
    st.subheader("📈 Base vs Surge Price Comparison")
    fig, ax = plt.subplots()
    prices = ["Base Price", "Surge Price"]
    values = [base_price, predicted_price]
    colors = ["purple", "blue"]

    ax.bar(prices, values, color=colors)
    ax.set_ylabel("Price (₹)")
    ax.set_title("Price Impact of Surge")
    st.pyplot(fig)



    # =====================================================
    # EXPLANATION
    # =====================================================
    st.info(
        f"""
        🔍 **Why this price?**
        - Demand/Supply Ratio: **{demand_supply_ratio:.2f}**
        - Time of Booking: **{time}**
        - Vehicle Type: **{vehicle}**
        - Location: **{location}**
        """
    )

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.caption("Dynamic Pricing Strategy Simulator | ML-powered Pricing Engine")

st.markdown("---")
st.markdown("Developed by **Keya Das** | Dynamic Pricing Strategy Simulator")

