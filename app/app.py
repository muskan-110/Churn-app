import streamlit as st
import pandas as pd
import pickle
import base64
from pathlib import Path



with open("model_xgboost.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)


st.set_page_config(page_title="Customer Churn Predictor", layout="wide")

def load_gif_base64(filename, width=50):
    """Convert a local GIF to base64 HTML image tag."""
    with open(filename, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f'<img src="data:image/gif;base64,{data}" width="{width}" style="vertical-align:middle; margin-right:10px;">'


stay_gif = load_gif_base64("icons/target-unscreen.gif", 60)     
churn_gif = load_gif_base64("icons/alert.gif", 60)      
sparkle_gif = load_gif_base64("icons/sparkle.gif", 40) 
    

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700;800&display=swap');
            

@keyframes gradientMove {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.stApp {
  background: #000000 ;
  background-size: 400% 400%  ;
  animation: gradientMove 20s ease infinite  ;
  font-family: 'Space Grotesk', sans-serif  ;
  min-height: 100vh  ;
}

.stApp, .stApp > header, .stApp [data-testid="stAppViewContainer"] {
  background: #000000  ;
  background-size: 400% 400%  ;
  animation: gradientMove 20s ease infinite  ;
}

[data-testid="stAppViewContainer"] {
  background: #000000  ;
  background-size: 400% 400%  ;
  animation: gradientMove 20s ease infinite  ;
}

[data-testid="stHeader"] {
  background: transparent  ;
}


.main .block-container {
  background: rgba(255, 255, 255, 0.5)  ;
  backdrop-filter: blur(20px)  ;
  border-radius: 30px  ;
  padding: 40px  ;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1)  ;
  border: 2px solid rgba(255, 255, 255, 0.7)  ;
  position: relative  ;
  z-index: 100  ;
}

.title {
    font-size: 60px !important  ;
    font-weight: 800  ;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%)  ;
    -webkit-background-clip: text  ;
    -webkit-text-fill-color: transparent  ;
    background-clip: text  ;
    text-align: center  ;
    margin-bottom: 5px  ;
    letter-spacing: -1px  ;
    font-family: 'Space Grotesk', sans-serif !important  ;
}


.subtitle {
    text-align: center  ;
    font-size: 1.5rem !important  ;
    color: #5a5a8f  ;
    margin-bottom: 40px  ;
    font-weight: 500  ;
}


label, .stSelectbox label, .stNumberInput label {
    color: #5a4b8a  ;
    font-weight: 600  ;
    font-size: 14px  ;
    text-transform: uppercase  ;
    letter-spacing: 0.5px  ;
    font-family: 'Space Grotesk', sans-serif  ;
}

div[data-baseweb="select"] > div {
    background: rgba(255, 255, 255, 0.9)  ;
    border: 3px solid #d4a5ff  ;
    border-radius: 15px  ;
    font-weight: 500  ;
    color: #5a4b8a  ;
    transition: all 0.3s ease  ;
}

div[data-baseweb="select"] > div:hover {
    border-color: #667eea  ;
    transform: translateY(-2px)  ;
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3)  ;
}

.stNumberInput > div > div > input {
    background: rgba(255, 255, 255, 0.9)  ;
    border: 3px solid #d4a5ff  ;
    border-radius: 15px  ;
    font-weight: 500  ;
    color: #5a4b8a  ;
    transition: all 0.3s ease  ;
    padding: 10px 15px  ;
}

.stNumberInput > div > div > input:hover {
    border-color: #667eea  ;
    transform: translateY(-2px)  ;
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3)  ;
}

.stNumberInput > div > div > input:focus {
    border-color: #667eea  ;
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3)  ;
}

input[type="number"] {
    background: rgba(255, 255, 255, 0.9)  ;
    color: #5a4b8a  ;
}

.stNumberInput button {
    background: rgba(212, 165, 255, 0.3)  ;
    color: #5a4b8a  ;
    border: none  ;
}

.stNumberInput button:hover {
    background: rgba(102, 126, 234, 0.4)  ;
}

.stButton {
    display: flex  ;
    justify-content: center  ;
    margin-top: 30px  ;
   
}
          

.stButton > button {
    width: 100%  ;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%)  ;
    color: white  ;
    font-size: 22px  ;
    font-weight: 700  ;
    border-radius: 20px  ;
    padding: 18px 20px  ;
    border: none  ;
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4)  ;
    transition: all 0.4s ease  ;
    text-transform: uppercase  ;
    letter-spacing: 1px  ;
    margin-top: 30px  ;
    align-self: center !important  ;
    display: flex !important  ;
    justify-content: center  ;
    font-family: 'Space Grotesk', sans-serif  ;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #f093fb 0%, #764ba2 50%, #667eea 100%)  ;
    transform: translateY(-5px) scale(1.02)  ;
    box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6)  ;
}

.result-box {
    border-radius: 25px  ;
    padding: 30px  ;
    margin-top: 30px  ;
    text-align: center  ;
    color: white  ;
    font-size: 22px  ;
    font-weight: 700  ;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2)  ;
    border: 4px solid rgba(255, 255, 255, 0.3)  ;
    animation: slideIn 0.6s ease  ;
    font-family: 'Space Grotesk', sans-serif  ;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Floating animation */
@keyframes float {
    0%, 100% { 
        transform: translate(0, 0) rotate(0deg); 
    }
    33% { 
        transform: translate(50px, -50px) rotate(120deg); 
    }
    66% { 
        transform: translate(-50px, 50px) rotate(240deg); 
    }
}


.floating-blob-1 {
    position: fixed  ;
    width: 500px  ;
    height: 500px  ;
    background: radial-gradient(circle, rgba(255, 100, 200, 0.5), rgba(255, 193, 227, 0.3), transparent)  ;
    border-radius: 50%  ;
    top: -200px  ;
    left: -200px  ;
    animation: float 15s ease-in-out infinite  ;
    z-index: 0  ;
    pointer-events: none  ;
}

.floating-blob-2 {
    position: fixed  ;
    width: 450px  ;
    height: 450px  ;
    background: radial-gradient(circle, rgba(100, 150, 255, 0.5), rgba(168, 216, 255, 0.3), transparent)  ;
    border-radius: 50%  ;
    bottom: -180px  ;
    right: -180px  ;
    animation: float 20s ease-in-out infinite reverse  ;
    z-index: 0  ;
    pointer-events: none  ;
}

.floating-blob-3 {
    position: fixed  ;
    width: 300px  ;
    height: 300px  ;
    background: radial-gradient(circle, rgba(200, 150, 255, 0.4), transparent)  ;
    border-radius: 50%  ;
    top: 40%  ;
    right: 10%  ;
    animation: float 18s ease-in-out infinite  ;
    z-index: 0  ;
    pointer-events: none  ;
}


/* All text to use Space Grotesk */
* {
    font-family: 'Space Grotesk', sans-serif  ;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="floating-blob-1"></div>
<div class="floating-blob-2"></div>
<div class="floating-blob-3"></div>
""", unsafe_allow_html=True)


# --- Header ---

st.markdown('<h1 class="title"> Customer Churn Prediction</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="subtitle">{sparkle_gif} Predict whether a customer will stay or churn using ML intelligence {sparkle_gif}</p>', unsafe_allow_html=True)



col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Partner", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=1)
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    TotalCharges = st.number_input("Total Charges", min_value=0.0, value=30.0)

with col2:
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=30.0)
    


new_data = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [SeniorCitizen],
    'Partner': [Partner],
    'Dependents': [Dependents],
    'tenure': [tenure],
    'PhoneService': [PhoneService],
    'MultipleLines': [MultipleLines],
    'InternetService': [InternetService],
    'OnlineSecurity': [OnlineSecurity],
    'OnlineBackup': [OnlineBackup],
    'DeviceProtection': [DeviceProtection],
    'TechSupport': [TechSupport],
    'StreamingTV': [StreamingTV],
    'StreamingMovies': [StreamingMovies],
    'Contract': [Contract],
    'PaperlessBilling': [PaperlessBilling],
    'PaymentMethod': [PaymentMethod],
    'MonthlyCharges': [MonthlyCharges],
    'TotalCharges': [TotalCharges]
})


for col, le in label_encoders.items():
    if col in new_data.columns:
        try:
            new_data[col] = le.transform(new_data[col])
        except Exception:
            new_data[col] = new_data[col].apply(lambda x: le.transform([x])[0] if x in le.classes_ else 0)

new_data = new_data.apply(pd.to_numeric, errors="coerce").fillna(0)


if st.button("🔍 Predict Churn"):
    pred = model.predict(new_data)[0]
    prob = model.predict_proba(new_data)[0][1]


    if pred == 1:
        st.markdown(f"""
        <div class="result-box" style="background: linear-gradient(135deg, #ff6b6b, #ee5a6f, #c44569);
                                       padding: 15px; border-radius: 12px;
                                       color: white; font-size: 18px; text-align: center;">
        {churn_gif} This customer is <b>likely to churn</b>.<br>
        Churn Probability: {prob:.2%}
        </div>
        """, unsafe_allow_html=True)
    else:
        
        st.markdown(f"""
        <div class="result-box" style="background: linear-gradient(135deg, #10b981, #34d399, #6ee7b7);
                                       padding: 15px; border-radius: 12px;
                                       color: white; font-size: 18px; text-align: center;">
        {stay_gif}
        <span style="vertical-align:middle;">This customer is <b>likely to stay</b>.<br>
        Retention Probability: {1 - prob:.2%}</span>
        </div>
        """, unsafe_allow_html=True)