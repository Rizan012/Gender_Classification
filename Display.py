import streamlit as st
import joblib
import numpy as np
import pandas as pd


model_gen = joblib.load("models/Gender1.pkl") 

st.title("Gender Classification Model")


hei = st.number_input("Enter your height (cm)", min_value=0.0, format="%.2f")
wei = st.number_input("Enter your weight (kg)", min_value=0.0, format="%.2f")


submit_button = st.button("Submit")

if submit_button:
    
    if hei > 0 and wei > 0:
        values = np.array([hei, wei]).reshape(1, -1)
        pred = model_gen.predict(values)
        st.write(f"You are a {pred[0]} :)")
    else:
        st.write("Please enter valid height and weight values.")
