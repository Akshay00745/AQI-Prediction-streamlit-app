# 🌍 Air Quality Index Prediction – End-to-End Deployment

## 🚀 Day 29 – 30 Days Data Science Challenge

This project demonstrates a complete end-to-end Machine Learning workflow — from data preprocessing and model training to deploying a real-time prediction web application using Streamlit.

The objective is to predict Air Quality Index (AQI proxy using RSPM) based on pollutant levels and environmental factors.

---

## 📊 Problem Statement

Air pollution is a major environmental and public health issue.  
This project aims to build a regression model that predicts AQI levels using historical pollutant data and deploy it as an interactive web application.

---

## 📂 Dataset Overview

The dataset contains:

- SO₂ levels
- NO₂ levels
- RSPM values (Target variable)
- State
- Area Type
- Monitoring station information

After cleaning:

- Dropped columns with excessive missing values
- Removed high-cardinality identifiers
- Handled missing values using median imputation
- Encoded categorical variables
- Reduced dataset size for efficient training

---

## 🧹 Data Preprocessing

- Removed columns with >50% missing values
- Dropped ID-like features (stn_code)
- Removed date columns (not required)
- Median imputation for pollutant levels
- One-hot encoding for categorical features
- Feature alignment saved for deployment

---

## 🤖 Model Training

Models compared:

- Linear Regression
- Random Forest Regressor

Model selection based on:

- RMSE (Root Mean Squared Error)
- R² Score

The best-performing model (based on lowest RMSE) was selected and saved using joblib.

---

## 📈 Model Evaluation Metrics

- RMSE
- R² Score

RMSE was used as the primary performance metric since it directly reflects average prediction error in AQI units.

---

## 🌐 Streamlit Web Application

The model was deployed using Streamlit.

Features of the app:

- User input for pollutant levels
- Dynamic prediction
- AQI category classification using if-else logic
- Feature alignment with trained model
- Cached model loading for efficiency

---

## 🛠 Tech Stack

- Python
- Pandas & NumPy
- Scikit-learn
- Joblib
- Streamlit

---

## 💡 Key Learnings

- End-to-end ML workflow implementation
- Model evaluation and selection using RMSE
- Handling large datasets efficiently
- Deployment considerations for performance
- Aligning preprocessing pipeline with deployment environment

---

## 🚀 Conclusion

This project demonstrates how machine learning models can be transformed from notebooks into real-world, user-interactive applications.

Building models is important — deploying them is essential.
