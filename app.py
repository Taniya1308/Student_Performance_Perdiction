import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Student Performance Predictor")

study_hours = st.number_input("Study Hours")
attendance = st.number_input("Attendance (%)")
previous_marks = st.number_input("Previous Marks")
sleep_hours = st.number_input("Sleep Hours")
social_media_hours = st.number_input("Social Media Hours")

if st.button("Predict"):
    input_data = np.array([[study_hours, attendance, previous_marks, sleep_hours, social_media_hours]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Score: {prediction[0]:.2f}")