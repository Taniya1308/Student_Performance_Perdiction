import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Student Predictor", page_icon="🎓")

# Title
st.title("🎓 Student Performance Predictor")
st.caption("Adjust inputs and see how performance changes")

st.divider()

# Inputs
hours = st.slider("📚 Weekly Study Hours", 0.0, 40.0, 5.0)
attendance = st.slider("📊 Attendance (%)", 0.0, 100.0, 75.0)
participation = st.slider("🙋 Class Participation", 0.0, 10.0, 5.0)

# Live Preview (this is the upgrade 🔥)
input_data = np.array([[hours, attendance, participation]])
prediction = model.predict(input_data)[0]

st.divider()

# Output
st.subheader("🎯 Predicted Score")
st.metric("Score", f"{prediction:.2f}")

# Visual indicator
st.progress(min(int(prediction), 100))

# Feedback
if prediction > 80:
    st.success("🌟 Excellent performance!")
elif prediction > 50:
    st.warning("⚠️ Average performance")
else:
    st.error("❗ Needs improvement")

# Insight section (THIS makes it interesting)
st.divider()
st.subheader("📈 Insights")

if hours < 5:
    st.info("Increase study hours for better results")
if attendance < 60:
    st.info("Low attendance is hurting performance")
if participation < 3:
    st.info("Try to participate more in class")