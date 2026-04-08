# Student_Performance_Perdiction

A machine learning project that predicts students’ final scores based on multiple factors such as study hours, attendance, previous marks, sleep hours, and social media usage. Built with **Python**, **scikit-learn**, and **Streamlit** for an interactive web app.

---

## 1. Project Overview

The goal of this project is to explore **machine learning for educational data** and create a tool that can estimate a student’s performance based on their habits and past academic records.  
Student performance depends on multiple factors, and this project models these relationships using **Linear Regression**.

---

## 2. Problem Definition

Predicting a student’s final score is a **regression problem** because the output (score) is continuous.  
Input features:

| Feature              | Description                             |
| -------------------- | --------------------------------------- |
| `study_hours`        | Number of hours a student studies daily |
| `attendance`         | Percentage of classes attended          |
| `previous_marks`     | Marks scored in previous exams          |
| `sleep_hours`        | Daily average sleep hours               |
| `social_media_hours` | Daily social media usage hours          |

Target variable:

| Feature       | Description                |
| ------------- | -------------------------- |
| `final_score` | Predicted final exam score |

---

## 3. Why Linear Regression?

- Simple and interpretable.
- Assumes a linear relationship between input features and the target variable.
- Allows examination of feature **coefficients** to understand impact.
- Can be upgraded to more advanced models if performance is poor (Polynomial Regression, Random Forest, Gradient Boosting).

---

## 4. How the Model Works

1. **Data Preparation**
   - Collect historical data of students.
   - Clean and normalize features if required.

2. **Train-Test Split**
   - Split data into training and testing sets to evaluate model performance.

3. **Model Training**
   - Train a **Linear Regression** model on the training set.

4. **Prediction**
   - Take user inputs in the Streamlit app.
   - Predict the student’s final score using the trained model.

5. **Evaluation**
   - Evaluate model using **R² score**, **Mean Absolute Error (MAE)**, and **Root Mean Squared Error (RMSE)**.

---

## 5. Streamlit Web App

The app allows users to **interactively input student data** and get predictions instantly.

- Input fields:
  - Study Hours
  - Attendance
  - Previous Marks
  - Sleep Hours
  - Social Media Hours
- Output: Predicted final score
- Uses a **pickle file** (`model.pkl`) to load the trained model.

---

## Installation

Follow these steps to set up and run the Student Performance Predictor app on your local machine.

### 6. Clone the repository

```bash
git clone https://github.com/Taniya1308/Student_Performance_Prediction.git
cd Student_Performance_Prediction
```
