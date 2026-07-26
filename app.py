# ==========================================================
# EduShield
# AI Powered Student Academic Risk Prediction System
# Flask Backend
# ==========================================================
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

# ===========================
# Load Model & Scaler
# ===========================
model = RandomForestClassifier()
model = joblib.load("models/best_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# ----------------------------------------------------------
# Create Flask Application
# ----------------------------------------------------------
app = Flask(__name__)

# ----------------------------------------------------------
# Home / Dashboard
# ----------------------------------------------------------
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# ----------------------------------------------------------
# Prediction Page
# ----------------------------------------------------------
@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None
    confidence = None
    risk_level = None
    recommendations = []

    if request.method == "POST":
        try:
            # Academic Information
            semester = int(request.form["semester"])
            age = int(request.form["age"])
            gender = int(request.form["gender"])
            attendance = float(request.form["attendance"])
            cgpa = float(request.form["cgpa"])
            internal_marks = float(request.form["internal_marks"])
            assignment_completion = float(request.form["assignment_completion"])
            study_hours = float(request.form["study_hours"])
            backlogs = int(request.form["backlogs"])

            # Psychological Information
            stress = int(request.form["stress"])
            motivation = int(request.form["motivation"])
            sleep = float(request.form["sleep_hours"])
            family_support = int(request.form["family_support"])

            # Lifestyle Information
            internet = int(request.form["internet_access"])
            extracurricular = int(request.form["extracurricular"])
            financial = int(request.form["financial_difficulty"])
            wellbeing = int(request.form["mental_wellbeing"])
            screen_time = float(request.form["screen_time"])
            commute = float(request.form["commute_time"])

            # Create DataFrame
            features = pd.DataFrame({
                "Semester": [semester],
                "Age": [age],
                "Gender": [gender],
                "Attendance_Percentage": [attendance],
                "Previous_CGPA": [cgpa],
                "Internal_Marks": [internal_marks],
                "Assignment_Completion": [assignment_completion],
                "Study_Hours_Per_Week": [study_hours],
                "Backlogs": [backlogs],
                "Stress_Level": [stress],
                "Motivation_Level": [motivation],
                "Sleep_Hours": [sleep],
                "Family_Support": [family_support],
                "Internet_Access": [internet],
                "Extracurricular": [extracurricular],
                "Financial_Difficulty": [financial],
                "Mental_Wellbeing": [wellbeing],
                "Screen_Time_Hours": [screen_time],
                "Commute_Time_Minutes": [commute]
            })

            # Scale Features
            scaled_features = scaler.transform(features)

            # Prediction
            pred = model.predict(scaled_features)[0]
            prob = model.predict_proba(scaled_features)[0]

            # 0 = Not At Risk, 1 = At Risk
            if pred == 0:
                prediction = "Not At Risk"
                confidence = round(prob[0] * 100, 2)
                risk_level = "Low"
            else:
                prediction = "At Risk"
                confidence = round(prob[1] * 100, 2)
                if confidence >= 85:
                    risk_level = "High"
                else:
                    risk_level = "Medium"

            # Recommendations
            recommendations = []

            if attendance < 75:
                recommendations.append("Improve attendance by attending lectures regularly.")
            if cgpa < 7:
                recommendations.append("Focus on improving CGPA through consistent study.")
            if internal_marks < 60:
                recommendations.append("Prepare better for internal assessments.")
            if assignment_completion < 80:
                recommendations.append("Complete assignments before the deadline.")
            if study_hours < 15:
                recommendations.append("Increase study hours to at least 15–20 hours per week.")
            if backlogs > 0:
                recommendations.append("Clear active backlogs as early as possible.")
            if stress > 7:
                recommendations.append("Practice stress management or seek counselling support.")
            if motivation < 5:
                recommendations.append("Set small academic goals to improve motivation.")
            if sleep < 7:
                recommendations.append("Aim for 7–8 hours of sleep daily.")
            if family_support < 5:
                recommendations.append("Seek support from mentors, teachers or academic advisors.")
            if screen_time > 8:
                recommendations.append("Reduce non-academic screen time.")
            if financial > 7:
                recommendations.append("Explore scholarships or financial aid opportunities.")
            if commute > 90:
                recommendations.append("Consider optimising travel time to reduce fatigue.")

            if len(recommendations) == 0:
                recommendations.append("Excellent! Continue maintaining your current academic performance.")

        except Exception as e:
            prediction = "Error"
            confidence = 0
            risk_level = "-"
            recommendations = [str(e)]

    return render_template(
        "predict.html",
        prediction=prediction,
        confidence=confidence,
        risk_level=risk_level,
        recommendations=recommendations
    )

# ----------------------------------------------------------
# Analytics Page
# ----------------------------------------------------------
@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

# ----------------------------------------------------------
# Explainable AI Page
# ----------------------------------------------------------
@app.route("/explain")
def explain():
    return render_template("explain.html")

# ----------------------------------------------------------
# About Page
# ----------------------------------------------------------
@app.route("/about")
def about():
    return render_template("about.html")

# ----------------------------------------------------------
# Run Flask Application
# ----------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)