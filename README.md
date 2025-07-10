# 🧠 Stack Overflow Tag Predictor

An AI-powered web app that **automatically predicts relevant tags** for Stack Overflow questions using **Machine Learning** and **Natural Language Processing**.

---

## 📌 Business Problem

Stack Overflow hosts millions of developer questions, but many are tagged incorrectly or inconsistently.  
Tags play a vital role in content organization, searchability, and directing questions to the right experts.  
However, **manual tagging is error-prone and time-consuming**, affecting content discoverability and user experience.

---

## 🎯 Project Goal

To build a smart, automated system that predicts relevant tags based on question content.  
The system aims to enhance **accuracy**, **speed**, and **consistency** in tag assignment using ML/NLP techniques.

---

## ✅ Objectives

- Predict **multiple relevant tags** from a question's text.
- Preprocess noisy HTML/code using **NLP techniques**.
- Use **TF-IDF + Logistic Regression** for efficient multi-label classification.
- Support real-time predictions via a **Streamlit web interface**.
- Ensure the solution is lightweight and deployment-ready.

---

## 📊 Data Understanding

| Feature | Description | Importance |
|--------|-------------|------------|
| `Body` | Main content of the question (may include code, text, HTML). | Primary input for prediction. |
| `Tags` | List of correct tags for the question. | Supervised multi-label target. |

---

## ⚙️ Model Pipeline

- **Text Cleaning**: Remove HTML tags, non-alphabetic characters, lowercase conversion  
- **Tokenization & Lemmatization**: Normalize words using NLTK  
- **TF-IDF Vectorization**: Convert processed text into feature vectors  
- **Multi-Label Classification**: One-vs-Rest strategy using Logistic Regression  
- **Evaluation**: Micro-averaged F1 Score

---

## 🖥️ Tech Stack

- **Programming**: Python  
- **Libraries**: Pandas, Scikit-learn, NLTK, BeautifulSoup  
- **Modeling**: TF-IDF, Logistic Regression  
- **UI**: Streamlit  
- **Model Persistence**: Joblib  
- **Deployment**: Hugging Face Spaces

---

## 🌟 Output

- **Predicted Tags**: e.g., `['python', 'pandas', 'dataframe']`  
- **Real-Time Prediction**: Users can input a question and receive instant tag predictions  
- **Lightweight App**: Fast and suitable for public demos or small-scale production

---

## 🚀 Deployment

The app is deployed on **Hugging Face Spaces** for live demo and usage.

>  🔗 [Live Demo Link](#) *(https://huggingface.co/spaces/Subh777/stackoverflow_tag_prediction)*

---
## 📝 License

This project is licensed under the [MIT License](LICENSE).



