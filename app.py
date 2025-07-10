import streamlit as st
import pandas as pd
from Description import run_Description
from EDA import run_EDA
from prediction import run_Prediction
from extra_features import run_ExtraFeatures

st.set_page_config(page_title="Stack Overflow Tag Predictor", layout="wide")

# 🌄 Global background image

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.pexels.com/photos/2473183/pexels-photo-2473183.jpeg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(255, 255, 255, 0.7); /* ✅ Correct rgba */
        z-index: -1;
    }
    </style>
""", unsafe_allow_html=True)





# Sidebar navigation
st.sidebar.title("📌 Navigation")
choice = st.sidebar.radio("Go to", [
    "📘 Description", 
    "📊 EDA", 
    "🤖 Prediction", 
    "🧠 Extra Features"
])

# Page router
if choice == "📘 Description":
    run_Description()
elif choice == "📊 EDA":
    df = pd.read_csv("stackoverflow_10k_sample.csv")
    run_EDA(df)
elif choice == "🤖 Prediction":
    run_Prediction()
elif choice == "🧠 Extra Features":
    run_ExtraFeatures()
