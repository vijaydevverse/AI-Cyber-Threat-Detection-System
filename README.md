# 🛡️ AI AutoML Security & Fraud Analyzer

An intelligent AutoML platform that automatically analyzes uploaded datasets, identifies target variables, performs data preprocessing, trains machine learning models, evaluates performance, and generates predictive insights through an interactive Streamlit dashboard.

Designed to simplify machine learning workflows, this application enables users to upload classification datasets and instantly build predictive models without writing code.

---

## 🚀 Features

### 📂 Dataset Upload

* Upload CSV datasets directly through the dashboard
* Supports various classification datasets
* Automatic dataset preview and exploration

### 🤖 Automated Machine Learning

* Automatic target column detection
* Intelligent preprocessing pipeline
* Automatic handling of categorical variables
* Label encoding for text-based features

### 📊 Model Training & Evaluation

* Random Forest Classification
* Automatic train-test split
* Accuracy evaluation
* Confusion Matrix generation
* Prediction analysis

### 📈 Data Visualization

* Interactive Feature Importance Chart
* Dataset Overview
* Performance Metrics Dashboard
* Prediction Results Visualization

### 📥 Export Results

* Download prediction results as CSV
* Save model outputs for further analysis

---

## 🏗️ Project Architecture

```text
AI AutoML Security & Fraud Analyzer
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── dashboard.png
```

---

## 🖥️ Dashboard Preview

![Dashboard](dashboard.png)

---

## ⚙️ Technology Stack

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* Random Forest Classifier

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Plotly

### Web Application Framework

* Streamlit

---

## 📋 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-AutoML-Security-Fraud-Analyzer.git
cd AI-AutoML-Security-Fraud-Analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 How It Works

1. Upload a CSV dataset.
2. The system automatically detects potential target variables.
3. Data preprocessing is performed automatically.
4. Categorical values are encoded.
5. A Random Forest model is trained.
6. Performance metrics are generated.
7. Feature importance is visualized.
8. Predictions are displayed and available for download.

---

## 📊 Supported Use Cases

* Cybersecurity Threat Detection
* Fraud Detection
* Customer Churn Prediction
* Credit Risk Assessment
* Employee Attrition Analysis
* Healthcare Classification
* General Machine Learning Classification Tasks

---

## 🔒 Key Capabilities

✔ Automated Dataset Analysis

✔ Automatic Target Detection

✔ Machine Learning Model Training

✔ Performance Evaluation

✔ Feature Importance Analysis

✔ Interactive Dashboard

✔ Prediction Export

✔ Beginner-Friendly Interface

---

## 🌟 Future Enhancements

* Multiple Algorithm Comparison
* Hyperparameter Optimization
* PDF Report Generation
* Model Persistence & Deployment
* Advanced AutoML Pipeline
* Explainable AI (XAI)
* ROC Curve & Precision-Recall Analysis
* Cloud Deployment Support

---

## 👨‍💻 Author

Developed as an AI & Data Science portfolio project demonstrating practical applications of:

* Machine Learning
* Data Analytics
* AutoML Systems
* Interactive Dashboard Development
* Python-Based Data Science Solutions

---

## 📜 License

This project is licensed under the MIT License.
