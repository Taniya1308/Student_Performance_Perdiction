# 🎓 Student Performance Predictor

## 📌 Overview

This project predicts a student's exam score based on:

- Weekly Study Hours
- Attendance Percentage
- Class Participation

It uses Machine Learning models and selects the best one based on performance.

---

## 🧠 Problem

Educational institutions need a way to identify students who may need support early.  
This project helps estimate student performance using study behavior data.

---

## 📊 Dataset

Features used:

- `weekly_self_study_hours`
- `attendance_percentage`
- `class_participation`

Target:

- `total_score`

---

## ⚙️ Models Used

- Linear Regression
- Decision Tree
- Random Forest (Final Model)

---

## 📈 Model Performance

| Model             | MAE  | RMSE | R² Score |
| ----------------- | ---- | ---- | -------- |
| Linear Regression | 3.33 | 4.02 | 0.93     |
| Decision Tree     | 4.17 | 5.70 | 0.86     |
| Random Forest     | 3.16 | 3.96 | 0.93     |

---

## 🏆 Final Model: Linear Regression

Although Random Forest showed slightly better performance, the difference was minimal.

Linear Regression was selected because:

- Comparable accuracy (very close RMSE and R²)
- Faster training and prediction
- Simpler and more interpretable
- Suitable for real-time applications

👉 Since the dataset shows a near-linear relationship, Linear Regression performs efficiently without unnecessary complexity.

---

## 🚀 Features

- Real-time prediction using Streamlit
- Interactive UI
- Instant performance feedback
- What-if analysis and insights

---

## 🛠 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
