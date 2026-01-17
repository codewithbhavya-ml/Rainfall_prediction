import streamlit as st
import pickle
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Rainfall Prediction App",
    page_icon="🌧️",
    layout="centered"
)

# Load trained model
with open("rainfall_model.pkl", "rb") as file:
    model = pickle.load(file)

# Feature columns (must match training)
columns = [
    "pressure",
    "dewpoint",
    "humidity",
    "cloud",
    "sunshine",
    "winddirection",
    "windspeed"
]

# App title
st.title("🌧️ Rainfall Prediction System")
st.write("Predict whether it will **rain or not** based on weather conditions.")

st.divider()

# Input fields
st.subheader("Enter Weather Parameters")

pressure = st.number_input("Pressure (hPa)", value=1000.0)
dewpoint = st.number_input("Dew Point (°C)", value=20.0)
humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=70)
cloud = st.number_input("Cloud Cover (%)", min_value=0, max_value=100, value=50)
sunshine = st.number_input("Sunshine (hours)", value=6.0)
winddirection = st.number_input("Wind Direction (degrees)", min_value=0, max_value=360, value=180)
windspeed = st.number_input("Wind Speed (km/h)", value=10.0)

# Predict button
if st.button("Predict Rainfall"):
    input_data = pd.DataFrame(
        [[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]],
        columns=columns
    )

    prediction = model.predict(input_data)[0]

    st.divider()

    if prediction == 1:
        st.success("🌧️ **Rainfall Expected**")
    else:
        st.info("☀️ **No Rainfall Expected**")

st.divider()
st.caption("Developed using Machine Learning & Streamlit")
