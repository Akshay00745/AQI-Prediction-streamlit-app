# =====================================
# 🌍 AQI Prediction Streamlit App
# =====================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -------------------------------------
# Page Config
# -------------------------------------
st.set_page_config(
    page_title="AQI Prediction App",
    page_icon="🌍",
    layout="centered"
)

# -------------------------------------
# Load Model & Features
# -------------------------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("aqi_model.pkl")
    features = joblib.load("model_features.pkl")
    return model, features

model, model_features = load_artifacts()

# -------------------------------------
# AQI Category Function
# -------------------------------------
def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good 🌿"
    elif aqi <= 100:
        return "Satisfactory 🙂"
    elif aqi <= 200:
        return "Moderate ⚠️"
    elif aqi <= 300:
        return "Poor 😷"
    elif aqi <= 400:
        return "Very Poor 🚨"
    else:
        return "Severe ☠️"

# -------------------------------------
# App Title
# -------------------------------------
st.title("🌍 Air Quality Index Prediction")
st.write("Enter pollutant levels to predict AQI (RSPM).")

# -------------------------------------
# User Inputs
# -------------------------------------
so2 = st.number_input("SO₂ Level", min_value=0.0, value=10.0)
no2 = st.number_input("NO₂ Level", min_value=0.0, value=20.0)

state = st.selectbox("State", ["Maharashtra", "Rajasthan", "Gujarat", "Delhi"])
area_type = st.selectbox("Area Type", ["Residential", "Industrial", "Sensitive", "Unknown"])

# -------------------------------------
# Prediction Logic
# -------------------------------------
if st.button("Predict AQI"):

    # Create base input dictionary
    input_dict = {
        "so2": so2,
        "no2": no2
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Encode categorical manually
    input_df = pd.get_dummies(
        input_df.assign(state=state, type=area_type),
        columns=["state", "type"]
    )

    # ---------------------------------
    # Align columns with trained model
    # ---------------------------------
    for col in model_features:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[model_features]

    # ---------------------------------
    # Predict
    # ---------------------------------
    prediction = model.predict(input_df)[0]

    category = get_aqi_category(prediction)

    # ---------------------------------
    # Display Result
    # ---------------------------------
    st.subheader("📊 Prediction Result")
    st.metric("Predicted AQI (RSPM)", round(prediction, 2))
    st.info(f"Air Quality Category: {category}")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Day 29 Project")