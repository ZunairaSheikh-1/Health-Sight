import streamlit as st
import pandas as pd
import pickle

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Car Prediction House", layout="wide")

# --- CUSTOM CSS: Black + Golden theme ---
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1552519507-da3b142c6e3d"); /* HD car image */
    background-size: cover;
    background-position: center;
}
h1, h2, h3, label, p {
    color: #FFD700 !important; /* Golden text */
    font-family: 'Arial Black', sans-serif;
}
button[kind="primary"] {
    background-color: #FFD700 !important;
    color: black !important;
    font-weight: bold !important;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- TITLE CENTER ---
st.markdown("<h1 style='text-align: center;'>🚗 AI Car Prediction House</h1>", unsafe_allow_html=True)

# --- SESSION STATE FOR PAGE SWITCH ---
if 'page' not in st.session_state:
    st.session_state.page = 1

# --- PAGE 1: Welcome Screen ---
if st.session_state.page == 1:
    st.subheader("👋 Enter Your Name to Continue:")
    customer_name = st.text_input("Name:")
    if customer_name:
        st.success(f"Welcome {customer_name} to AI Car Prediction House!")
        if st.button("Next ➡️"):
            st.session_state.page = 2

# --- PAGE 2: Car Details + Map ---
elif st.session_state.page == 2:
    st.subheader("📝 Enter Car Details:")
    col1, col2 = st.columns(2)
    with col1:
        # Car Model Dropdown (Large List)
        car_model = st.selectbox(
            "Select Car Model:",
            [
                "Toyota Corolla", "Honda Civic", "Honda City", "Suzuki Alto", "Suzuki Mehran",
                "Suzuki WagonR", "Suzuki Cultus", "Suzuki Swift", "Toyota Yaris", "Toyota Fortuner",
                "Toyota Hilux Revo", "Kia Sportage", "Kia Sorento", "Hyundai Tucson",
                "Hyundai Elantra", "Hyundai Sonata", "MG HS", "MG ZS", "DFSK Glory 580",
                "Prince Pearl", "Changan Alsvin", "Changan Oshan X7", "Proton Saga", "Proton X70",
                "Nissan Dayz", "Daihatsu Mira", "Other"
            ]
        )
        year = st.number_input("Manufacturing Year", min_value=1900, max_value=2024, value=2015)
        present_price = st.number_input("Current Selling Price (in Lakhs):", min_value=0.0, value=10.0)
        kms_driven = st.number_input("Kilometers Driven:", min_value=0, value=50000)
    with col2:
        fuel_type = st.selectbox("Fuel Type:", ['Petrol', 'Diesel', 'CNG'])
        seller_type = st.selectbox("Seller Type:", ['Dealer', 'Individual'])
        transmission = st.selectbox("Transmission Type:", ['Manual', 'Automatic'])
        owner = st.number_input("Number of Previous Owners:", min_value=0, value=0)

    # --- MODEL LOADING ---
    try:
        with open("lasso_regression_model.pkl", "rb") as file:
            model = pickle.load(file)
    except FileNotFoundError:
        st.error("Model file 'lasso_regression_model.pkl' not found. Please upload the trained model.")
        st.stop()

    # --- ENCODING ---
    fuel_type_map = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
    seller_type_map = {'Dealer': 0, 'Individual': 1}
    transmission_map = {'Manual': 0, 'Automatic': 1}

    input_df = pd.DataFrame([[ 
        year, present_price, kms_driven, 
        fuel_type_map[fuel_type], seller_type_map[seller_type], 
        transmission_map[transmission], owner 
    ]], columns=['Year', 'Present_Price', 'Kms_Driven', 
                 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner'])

    if st.button("💰 Predict Price"):
        predicted_price = model.predict(input_df)
        st.success(f"💰 Predicted Selling Price for {car_model}: {predicted_price[0]:.2f} Lakhs")

    # --- MAP INPUT (city dropdown instead of lat/lon) ---
    st.subheader("📍 Select Your City:")
    cities = {
        "Lahore": (31.5204, 74.3587),
        "Karachi": (24.8607, 67.0011),
        "Islamabad": (33.6844, 73.0479),
        "Faisalabad": (31.4180, 73.0791),
        "Multan": (30.1575, 71.5249),
        "Peshawar": (34.0151, 71.5249),
        "Quetta": (30.1798, 66.9750),
        "Sialkot": (32.4927, 74.5319),
        "Rawalpindi": (33.6007, 73.0679)
    }
    city = st.selectbox("Choose City:", list(cities.keys()))
    lat, lon = cities[city]
    st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}))

    if st.button("⬅️ Back"):
        st.session_state.page = 1

      











