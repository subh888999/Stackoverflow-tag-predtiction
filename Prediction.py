import pandas as pd
import ast
import re
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
import joblib
import streamlit as st

# -----------------------------
# 🔄 Download NLTK Resources (for deployment platforms like Hugging Face)
# -----------------------------
nltk.download("stopwords")
nltk.download("wordnet")

# -----------------------------
# 📦 Text Preprocessing
# -----------------------------
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = BeautifulSoup(str(text), "html.parser").get_text()
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower()
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return " ".join(tokens)

# -----------------------------
# 🚀 Streamlit UI + Model Loaders
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("logistic_full_model.pkl")

@st.cache_resource
def load_vectorizer():
    return joblib.load("tfidf.pkl")

@st.cache_resource
def load_mlb():
    return joblib.load("mlb.pkl")

# -----------------------------
# 🧠 Prediction App Function
# -----------------------------
def run_Prediction():
    st.set_page_config(page_title="Stack Overflow Tag Predictor", layout="centered")
    st.title("🧠 Stack Overflow Tag Predictor")
    st.write("Enter a Stack Overflow question body to predict relevant tags.")

    user_input = st.text_area("Your Question Body:", height=150)

    if st.button("Predict Tags"):
        if user_input.strip():
            with st.spinner("Predicting..."):
                cleaned = clean_text(user_input)
                tfidf = load_vectorizer()
                X_new = tfidf.transform([cleaned])
                model = load_model()
                mlb = load_mlb()
                pred = model.predict(X_new)
                tags = mlb.inverse_transform(pred)
                st.success(f"Predicted Tags: {tags[0] if tags else 'No tags predicted'}")
        else:
            st.warning("Please enter a question before predicting.")
