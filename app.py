import streamlit as st
import numpy as np
import joblib

model = joblib.load("churn_model.pkl")

st.title("🏦 Bank Mijozlari Churn Bashorati")

credit = st.number_input("Credit Score")
age = st.number_input("Age")
balance = st.number_input("Balance")
products = st.number_input("Products")
active = st.selectbox("Active Member", [0,1])

if st.button("Predict"):
    data = np.array([[credit, age, balance, products, active]])
    result = model.predict(data)

    if result[0] == 1:
        st.error("❌ Mijoz ketadi (High Risk)")
    else:
        st.success("✅ Mijoz qoladi (Low Risk)")
