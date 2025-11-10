 Customer Churn Prediction using Machine Learning

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn or stay, built using XGBoost for model training and Streamlit for a fully interactive web interface.

🌐 Live Demo : https://churn-app-3umtgwznfthd2epx8fyu88.streamlit.app/


🏗️ Project Overview

This project demonstrates a complete ML pipeline — from data preprocessing and feature encoding to model training, evaluation, and deployment through an intuitive Streamlit dashboard.

It aims to help telecom companies identify customers who are likely to discontinue services and take proactive retention actions.

🧩 Key Features

1. Interactive Streamlit Frontend – Clean, modern UI for easy data input and churn prediction
2. XGBoost Model – Trained for high accuracy and robustness
3. Label Encoding for Categorical Variables – Consistent mapping across train and inference stages
4. Imbalanced Data Handling – Applied SMOTE (Synthetic Minority Oversampling Technique) to balance churn vs. non-churn classes
5. Modular Codebase – Easy to maintain, modify, and extend

📊 Data Processing & Model Training

All data cleaning, preprocessing, and model training steps are documented in the Colab Notebook
.
Here’s a summary of what was done:

1️⃣ Data Cleaning

Handled missing values in TotalCharges

Converted data types where necessary (e.g., numeric conversion of strings)

Removed redundant or highly correlated columns

2️⃣ Feature Engineering

Encoded categorical features using LabelEncoder

Created derived features such as tenure groups

Normalized numeric values to improve model convergence

3️⃣ Handling Imbalanced Data

Used SMOTE to oversample minority churn cases and achieve balanced class distribution

4️⃣ Model Selection

Trained multiple models (Decision Tree, Random Forest, XGBoost)

Selected XGBoost due to superior performance on accuracy

5️⃣ Model Evaluation

Evaluated using:

Accuracy

Precision / Recall / F1-score

Confusion Matrix


6️⃣ Model Export

Saved final model and label encoders as:

model_xgboost.pkl

label_encoders.pkl

These are later used by the Streamlit app for real-time predictions.

🎨 Streamlit Frontend

The app allows users to input customer details and get instant predictions.

⚙️ Tech Stack
   Component	              Technology
1. Frontend	              Streamlit
2. Backend / Model	       XGBoost, Scikit-learn
3. Data Handling	         Pandas, NumPy
4. Visualization	         Matplotlib, Seaborn
5. Deployment	            Streamlit Cloud
6. Environment	           Python 3.10+

