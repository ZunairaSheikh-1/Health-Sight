import streamlit as st
import pandas as pd
import pickle
# Custom CSS for background color and title style
page_bg = """
<style>
body, [data-testid="stAppViewContainer"] {
    background-color: #800080 !important; /* purple background */
    color: #ffffff !important; /* default text color white */
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0); /* transparent header */
}
h1 {
    color: orange !important;
    text-align: center;
    font-family: 'Arial Black', sans-serif;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)
# Load the trained model
try:
    with open('lasso_regression_model.pkl', 'rb') as file:
        lass_reg_model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file 'lasso_regression_model.pkl' not found. Please make sure the model is saved.")
    st.stop()
# Title of the web app
st.title("🚗 Smart AI Car Price Calculator App")
# Get input from the user
year = st.number_input("Enter the manufacturing year of the car:", min_value=1900, max_value=2024, value=2015)
present_price = st.number_input("Enter the current selling price (in Lakhs):", min_value=0.0, value=10.0)
kms_driven = st.number_input("Enter the number of kilometers driven:", min_value=0, value=50000)
fuel_type = st.selectbox("Select the fuel type:", ['Petrol', 'Diesel', 'CNG'])
seller_type = st.selectbox("Select the seller type:", ['Dealer', 'Individual'])
transmission = st.selectbox("Select the transmission type:", ['Manual', 'Automatic'])
owner = st.number_input("Enter the number of previous owners (0 for first owner):", min_value=0, value=0)
# Mapping categorical inputs to numerical values
fuel_type_map = {'Petrol':0, 'Diesel':1, 'CNG':2}
seller_type_map = {'Dealer':0, 'Individual':1}
transmission_map = {'Manual':0, 'Automatic':1}
fuel_type_encoded = fuel_type_map[fuel_type]
seller_type_encoded = seller_type_map[seller_type]
transmission_encoded = transmission_map[transmission]
# Create a DataFrame from the input
input_data = pd.DataFrame(
    [[year, present_price, kms_driven, fuel_type_encoded, seller_type_encoded, transmission_encoded, owner]],
    columns=['Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']
)
# Predict the selling price
if st.button("Predict Price"):
    predicted_price = lass_reg_model.predict(input_data)
    st.success(f"💰 Predicted Selling Price: {predicted_price[0]:.2f} Lakhs")