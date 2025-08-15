import streamlit as st
import requests

# FastAPI backend URL (change to Render URL after deployment)
BACKEND_URL = "http://localhost:8000"

st.title("💓 Heart Disease Prediction")
st.write("Enter patient details to predict heart disease presence.")

# Create input fields
age = st.number_input("Age", 1, 120, 50)
sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", 80, 200, 120)
chol = st.number_input("Serum Cholesterol (chol)", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG Results (restecg)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved (thalach)", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 10.0, 1.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise (slope)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels Colored (ca)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

if st.button("Predict"):
    payload = {
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps,
        "chol": chol, "fbs": fbs, "restecg": restecg,
        "thalach": thalach, "exang": exang, "oldpeak": oldpeak,
        "slope": slope, "ca": ca, "thal": thal
    }
    try:
        response = requests.post(f"{BACKEND_URL}/predict", json=payload)
        if response.status_code == 200:
            result = response.json()["heart_disease"]
            if result:
                st.error("⚠️ Heart Disease Detected")
            else:
                st.success("✅ No Heart Disease Detected")
        else:
            st.error("Error: Could not get prediction")
    except Exception as e:
        st.error(f"Request failed: {e}")
