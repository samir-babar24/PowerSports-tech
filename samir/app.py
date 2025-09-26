import streamlit as st
import pickle
import numpy as np

# Load model
import pickle


import joblib
import os

# Get current directory of app.py
BASE_DIR = os.path.dirname(__file__)

# Model path (same folder as app.py)
model_path = os.path.join(BASE_DIR, "samir_model.pkl")

# Load model
model = joblib.load(model_path)



# Page config
st.set_page_config(page_title="Gym Experience Predictor", page_icon="🏋️", layout="wide")

# Custom dark theme CSS
st.markdown("""
    <style>
        body {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        .stTextInput, .stNumberInput, .stSelectbox {
            background-color: #262730 !important;
            border-radius: 10px;
            padding: 5px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #FF4B4B, #FF914D);
            color: white;
            font-weight: bold;
            border-radius: 12px;
            padding: 0.6em 1.2em;
            transition: 0.3s;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background: linear-gradient(90deg, #FF914D, #FF4B4B);
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color:#FF914D;'>🏋️ Gym Experience Level Predictor</h1>", unsafe_allow_html=True)
st.write("Fill in your details and get your predicted **Experience Level**: Beginner / Intermediate / Expert.")

# Layout in 3 sections
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("👤 Personal Info")
    age = st.number_input("Age (years)")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    weight = st.number_input("Weight (kg)")
    height = st.number_input("Height (m)")
    bmi = st.number_input("BMI (kg/m²)")
    fat_percent = st.number_input("Body Fat Percentage (%)")

with col2:
    st.subheader(" Health Metrics")
    max_bpm = st.number_input("Maximum Heart Rate (BPM)")
    avg_bpm = st.number_input("Average Heart Rate (BPM)")
    resting_bpm = st.number_input("Resting Heart Rate (BPM)")
    water_intake = st.number_input("Daily Water Intake (liters)")

with col3:
    st.subheader(" Workout Info")
    session_duration = st.number_input("Workout Session Duration (hours)")
    calories = st.number_input("Calories Burned")
    workout_type = st.selectbox("Workout Type", ["Yoga", "HIIT", "Cardio", "Strength Training"])
    workout_freq = st.number_input("Workout Frequency (days/week)")

# Encoding
gender_map = {"Male": 0, "Female": 1, "Other": 2}
workout_map = {"Yoga": 0, "HIIT": 1, "Cardio": 2, "Strength Training": 3}

gender_val = gender_map[gender]
workout_val = workout_map[workout_type]

# Prediction button
if st.button(" Predict Experience Level"):
    features = np.array([[age, gender_val, weight, height, max_bpm, avg_bpm, resting_bpm,
                          session_duration, calories, workout_val, fat_percent,
                          water_intake, workout_freq, bmi]])
    
    prediction = model.predict(features)[0]
    mapping = {1: "Beginner", 2: "Intermediate", 3: "Expert"}
    
    st.markdown(f"<h2 style='text-align: center; color:#00FFB0;'>🏆 Predicted Experience Level: {mapping[prediction]}</h2>", unsafe_allow_html=True)

