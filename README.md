# 🎓 Student Performance Predictor

## 📌 Overview

This project predicts a student's final exam score based on:

- Weekly Study Hours
- Attendance Percentage
- Class Participation

It uses multiple Machine Learning models and compares their performance to select the best one.

---

## 🧠 Problem Statement

Educational institutions often want to predict student performance early to provide support.  
This project builds a predictive model to estimate student scores based on behavioral and academic factors.

---

## 📊 Dataset

The dataset contains the following features:

- `weekly_self_study_hours`
- `attendance_percentage`
- `class_participation`
- `total_score` (Target)

---

## ⚙️ Models Used

### 1️⃣ Linear Regression

- Assumes a linear relationship between input features and output
- Simple and fast
- Works well when data is linear

---

### 2️⃣ Decision Tree Regressor

- Splits data into multiple conditions
- Captures non-linear relationships
- Can overfit if not controlled

---

### 3️⃣ Random Forest Regressor ✅ (Final Model)

- Ensemble of multiple decision trees
- Reduces overfitting
- Handles complex patterns better

---

## 📈 Model Performance

| Model             | MAE  | RMSE | R² Score |
| ----------------- | ---- | ---- | -------- |
| Linear Regression | 3.33 | 4.02 | 0.93     |
| Decision Tree     | 4.17 | 5.70 | 0.86     |
| Random Forest     | 3.16 | 3.96 | 0.93     |

---

## 🏆 Best Model: Random Forest

### Why Random Forest?

- Lowest RMSE → better at handling large errors
- Highest R² → explains data well
- More robust than Decision Tree
- Captures non-linear relationships better than Linear Regression

👉 Even though Linear Regression is close, Random Forest performs slightly better and is more reliable.

---

## 🚀 Features

- Real-time prediction using Streamlit
- Interactive UI with sliders
- Instant feedback (Excellent / Average / Needs Improvement)
- Data-driven model comparison

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
