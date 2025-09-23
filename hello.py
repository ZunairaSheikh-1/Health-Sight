import streamlit as st
import pandas as pd
import pickle

# Custom CSS for styling
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #2c003e, #800080, #d147a3);
    color: #ffffff;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
h1 {
    color: #FFD700 !important;
    text-align: center;
    font-family: 'Trebuchet MS', sans-serif;
    font-size: 48px !important;
    text-shadow: 2px 2px 5px #000000;
}
h2, h3, label {
    color: #ffccff !important;
    font-family: 'Verdana', sans-serif;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Load the trained model
try:
    with open('lasso_regression_model.pkl', 'rb') as file:
        lass_reg_model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file 'lasso_regression_model.pkl' not found. Please make sure it exists.")
    st.stop()

# 🌟 Title of the web app
st.title("Welcome to Car House – Smart AI Price Predictor")

st.write("Get the **best estimated resale value** of your car instantly with AI-powered predictions.")

# Sidebar inputs
st.sidebar.header("Car Details Input")
year = st.sidebar.number_input("Manufacturing Year:", min_value=1900, max_value=2024, value=2015)
present_price = st.sidebar.number_input("Current Price (in Lakhs):", min_value=0.0, value=10.0)
kms_driven = st.sidebar.number_input("Kilometers Driven:", min_value=0, value=50000)

fuel_type = st.sidebar.selectbox("Fuel Type:", ['Petrol', 'Diesel', 'CNG'])
seller_type = st.sidebar.selectbox("Seller Type:", ['Dealer', 'Individual'])
transmission = st.sidebar.selectbox("Transmission:", ['Manual', 'Automatic'])
owner = st.sidebar.number_input("No. of Previous Owners:", min_value=0, value=0)

# Encode categorical inputs
fuel_type_map = {'Petrol':0, 'Diesel':1, 'CNG':2}
seller_type_map = {'Dealer':0, 'Individual':1}
transmission_map = {'Manual':0, 'Automatic':1}

fuel_type_encoded = fuel_type_map[fuel_type]
seller_type_encoded = seller_type_map[seller_type]
transmission_encoded = transmission_map[transmission]

#Create DataFrame
input_data = pd.DataFrame(
    [[year, present_price, kms_driven, fuel_type_encoded, seller_type_encoded, transmission_encoded, owner]],
    columns=['Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']
)

# Predict Price
if st.button("redict Car Value"):
    predicted_price = lass_reg_model.predict(input_data)
    st.success(f"Predicted Selling Price: **{predicted_price[0]:.2f} Lakhs**")
    st.balloons()
    st.info("Tip: Cars with **fewer kilometers** and **first owners** usually get a higher resale value!")

