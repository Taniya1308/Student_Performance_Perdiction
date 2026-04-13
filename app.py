import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Student Predictor", page_icon="🎓")

st.title("🎓 Student Performance Predictor")
st.caption("Experiment with inputs and see how performance changes in real-time")

st.divider()

# Inputs
hours = st.slider("📚 Weekly Study Hours", 0.0, 40.0, 5.0)
attendance = st.slider("📊 Attendance (%)", 0.0, 100.0, 75.0)
participation = st.slider("🙋 Class Participation", 0.0, 10.0, 5.0)

# Prediction
input_data = np.array([[hours, attendance, participation]])
prediction = model.predict(input_data)[0]

st.divider()

# Output
st.subheader("🎯 Predicted Score")
st.metric("Score", f"{prediction:.2f}")
st.progress(min(int(prediction), 100))

# Feedback
if prediction > 80:
    st.success("🌟 Excellent performance!")
elif prediction > 50:
    st.warning("⚠️ Average performance")
else:
    st.error("❗ Needs improvement")

# 🔥 NEW: What-if Analysis
st.divider()
st.subheader("🔍 What if you improve?")

col1, col2 = st.columns(2)

with col1:
    if st.button("Increase Study Hours +5"):
        new_pred = model.predict(np.array([[hours+5, attendance, participation]]))[0]
        st.info(f"New Score: {new_pred:.2f}")

with col2:
    if st.button("Improve Attendance to 90%"):
        new_pred = model.predict(np.array([[hours, 90, participation]]))[0]
        st.info(f"New Score: {new_pred:.2f}")

# 🔥 NEW: Performance Breakdown (simple logic)
st.divider()
st.subheader("📊 Performance Breakdown")

st.write(f"Study Contribution: {hours * 2:.1f}")
st.write(f"Attendance Contribution: {attendance * 0.5:.1f}")
st.write(f"Participation Contribution: {participation * 3:.1f}")

# 🔥 Insights
st.divider()
st.subheader("📈 Insights")

if hours < 5:
    st.info("Increase study hours for better results")
if attendance < 60:
    st.info("Low attendance is hurting performance")
if participation < 3:
    st.info("Try to participate more in class")

# 🔥 Warning for unrealistic input
if hours > 25:
    st.warning("⚠️ Very high study hours — may not be realistic")