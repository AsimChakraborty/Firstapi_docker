# 💓 Heart Disease Prediction API & Web App

This project is a **machine learning-powered** heart disease prediction system, built with:

- **FastAPI** (Backend API for ML predictions)
- **Streamlit** (Frontend UI for user interaction)
- **Docker & Docker Compose** (Containerization)


---

## 📌 Objective
To create a simple, deployable application where users can input medical parameters and get a prediction on the likelihood of having heart disease.

---

## 🏗 Features
- **FastAPI Backend**:
  - `/health` → Check API health
  - `/info` → Model info & features
  - `/predict` → Predict heart disease (True/False)

- **Streamlit Frontend**:
  - User-friendly form to enter patient details
  - Real-time prediction results
 
🧠 Train the Model

python training/train_model.py

⚙️ Start the FastAPI Server

uvicorn app.main:app --reload

🌐 Start the Streamlit Frontend

streamlit run streamlit_app/frontend.py

- **Dockerized**:
  - Run locally using `docker-compose`
  - Deploy to Render or any cloud platform

---
