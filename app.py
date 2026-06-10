import streamlit as st
import numpy as np
import pickle

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Student Predictor", page_icon="🎓", layout="centered")

# ---------------- SIMPLE SAFE CSS (ONLY COLORS, NO BREAKING LAYOUT) ----------------
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
    }

    h1 {
        color: #38bdf8;
    }

    .stMetric {
        background-color: #1e293b;
        padding: 12px;
        border-radius: 10px;
    }

    </style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------- TITLE ----------------
st.title("🎓 Student Performance Predictor")
st.caption("AI model predicts student score based on academic behavior")

st.divider()

# ---------------- INPUTS ----------------
hours = st.slider("📚 Weekly Study Hours", 0.0, 40.0, 5.0)
attendance = st.slider("📊 Attendance (%)", 0.0, 100.0, 75.0)
participation = st.slider("🙋 Class Participation", 0.0, 10.0, 5.0)

# ---------------- PREDICTION ----------------
input_data = np.array([[hours, attendance, participation]])
prediction = model.predict(input_data)[0]

st.divider()

# ---------------- RESULT CARD ----------------
st.subheader("🎯 Predicted Score")

# colored metric using logic
if prediction > 80:
    st.success(f"🌟 Excellent Score: {prediction:.2f}")
elif prediction > 50:
    st.warning(f"⚠️ Average Score: {prediction:.2f}")
else:
    st.error(f"❗ Low Score: {prediction:.2f}")

st.progress(min(int(prediction), 100))

# ---------------- METRICS ROW ----------------
col1, col2, col3 = st.columns(3)

col1.metric("📚 Study", f"{hours:.1f}")
col2.metric("📊 Attendance", f"{attendance:.1f}%")
col3.metric("🙋 Participation", f"{participation:.1f}")

st.divider()

# ---------------- WHAT IF SECTION ----------------
st.subheader("🔍 What-If Analysis")

col1, col2 = st.columns(2)

with col1:
    if st.button("📈 Increase Study +5"):
        new_pred = model.predict(np.array([[hours+5, attendance, participation]]))[0]
        st.info(f"New Score: {new_pred:.2f}")

with col2:
    if st.button("📊 Attendance → 90%"):
        new_pred = model.predict(np.array([[hours, 90, participation]]))[0]
        st.info(f"New Score: {new_pred:.2f}")

st.divider()

# ---------------- BREAKDOWN ----------------
st.subheader("📊 Performance Breakdown")

st.markdown(f"""
<div style="background-color:#1e293b;padding:15px;border-radius:10px;color:white">
<ul>
<li>📚 Study Contribution: <b>{hours * 2:.1f}</b></li>
<li>📊 Attendance Contribution: <b>{attendance * 0.5:.1f}</b></li>
<li>🙋 Participation Contribution: <b>{participation * 3:.1f}</b></li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------------- INSIGHTS ----------------
st.subheader("📈 Insights")

if hours < 5:
    st.info("📚 Increase study hours to improve score")
if attendance < 60:
    st.warning("📊 Low attendance affecting performance")
if participation < 3:
    st.info("🙋 Increase class participation")

if hours > 25:
    st.warning("⚠️ Unrealistic study hours detected")