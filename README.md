 Customer Churn Prediction using Machine Learning

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn or stay, built using XGBoost for model training and Streamlit for a fully interactive web interface.

🌐 Live Demo : https://churn-app-3umtgwznfthd2epx8fyu88.streamlit.app/


🏗️ Project Overview

This project demonstrates a complete ML pipeline — from data preprocessing and feature encoding to model training, evaluation, and deployment through an intuitive Streamlit dashboard.

It aims to help telecom companies identify customers who are likely to discontinue services and take proactive retention actions.

🧩 Key Features

✅ Interactive Streamlit Frontend – Clean, modern UI for easy data input and churn prediction
✅ XGBoost Model – Trained for high accuracy and robustness
✅ Label Encoding for Categorical Variables – Consistent mapping across train and inference stages
✅ Imbalanced Data Handling – Applied SMOTE (Synthetic Minority Oversampling Technique) to balance churn vs. non-churn classes
✅ Modular Codebase – Easy to maintain, modify, and extend

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

Prediction Logic

When the “Predict Churn” button is clicked:

User input is converted into a DataFrame.

Label Encoders transform categorical values.

The trained XGBoost model predicts churn probability.

⚙️ Tech Stack
Component	              Technology
Frontend	              Streamlit
Backend / Model	          XGBoost, Scikit-learn
Data Handling	          Pandas, NumPy
Visualization	          Matplotlib, Seaborn
Deployment	              Streamlit Cloud
Environment	              Python 3.10+


🚀 Run Locally
1️⃣ Clone the repository
git clone https://github.com/yourusername/customer-churn-app.git
cd customer-churn-app/app

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run app.py


Then open http://localhost:8501 in your browser.
