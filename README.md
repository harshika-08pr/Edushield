# 🎓 EduShield – AI-Powered Student Performance Prediction System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![XGBoost](https://img.shields.io/badge/XGBoost-Machine%20Learning-green?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-AI-orange?style=for-the-badge&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

### Predict • Analyze • Explain • Recommend

An intelligent web application that predicts students at academic risk using Machine Learning and provides explainable insights along with personalized recommendations to improve performance.

</div>

---

## 📌 Project Overview

EduShield is an AI-driven educational analytics platform developed to assist institutions in identifying students who may be academically at risk.

The application uses an **XGBoost Machine Learning model** trained on student-related features to predict academic risk. It also provides visual analytics, explainable AI using SHAP, and personalized recommendations that help educators make informed decisions.

---

## ✨ Key Features

- 🧠 AI-based Student Risk Prediction
- 📊 Interactive Analytics Dashboard
- 💡 Explainable AI (SHAP Feature Importance)
- 🎯 Personalized Academic Recommendations
- 📈 ROC Curve & Model Performance Visualization
- 🌐 Responsive Flask Web Interface
- ⚡ Fast Predictions using Trained Model (.pkl)

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- XGBoost Classifier
- Scikit-learn
- Pandas
- NumPy

### Explainable AI
- SHAP

### Visualization
- Matplotlib

---

## 📂 Project Structure

```
EduShield/
│
├── app.py
├── requirements.txt
├── EduShield_Enhanced_Dataset.csv
├── Edushield.ipynb
│
├── models/
│   ├── best_model.pkl
│   └── scaler.pkl
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── templates/
    ├── base.html
    ├── index.html
    ├── dashboard.html
    ├── predict.html
    ├── analytics.html
    ├── explain.html
    ├── recommendation.html
    └── about.html
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/harshika-08pr/Edushield.git
```

```bash
cd Edushield
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Scaling
4. Model Training
5. XGBoost Classification
6. Model Evaluation
7. Explainability using SHAP
8. Deployment using Flask

---

## 📈 Model Outputs

The application provides:

- Student Risk Prediction
- Model Accuracy Comparison
- ROC Curve
- SHAP Feature Importance
- Personalized Academic Suggestions

---

## 📷 Application Pages

- 🏠 Home
- 📊 Dashboard
- 🧠 Prediction
- 📈 Analytics
- 💡 Explainable AI
- 🎯 Recommendations
- ℹ️ About

---

## 📚 Future Enhancements

- User Authentication
- Student Login Portal
- Teacher Dashboard
- Real-time Database Integration
- Cloud Deployment
- Email Alerts for At-Risk Students
- AI Chatbot Support

---

## 👩‍💻 Author

**Harshika**

B.Tech CSE (Artificial Intelligence & Machine Learning)

KIET Group of Institutions, Ghaziabad

GitHub: https://github.com/harshika-08pr

LinkedIn: https://www.linkedin.com/in/harshika-panwar-0208h/

---

## ⭐ If you found this project useful

Please consider giving this repository a **⭐ Star** on GitHub.

It motivates me to build more AI and Machine Learning projects.

---

## 📄 License

This project is developed for educational and learning purposes.

MIT License.
