import streamlit as st

def run_ExtraFeatures():
    st.set_page_config(page_title="Advanced Features", layout="centered")

    st.title("🔧 Extra Features & Advancements")
    st.markdown("---")

    st.markdown("""
    This page highlights the extended capabilities and future-proof aspects of the **Stack Overflow Tag Prediction** project.
    """)

    st.markdown("### 💡 Advanced Features")

    st.markdown("""
    - ✨ **Interactive Tag Filtering**  
      Enables users to explore and filter questions by specific tags in the EDA interface.
    - 🧠 **Expandable to Transformers/BERT**  
      The pipeline can be upgraded to use advanced NLP models like BERT or DistilBERT for higher tag prediction accuracy.
    - ⚖️ **Class Imbalance Handling**  
      Tags with low frequency are filtered to improve precision and reduce noise in predictions.
    - 🗃️ **Multi-Hot Label Representation**  
      Uses `MultiLabelBinarizer` to encode multiple tags per question for multi-label classification.
    - 📁 **Pluggable Dataset Support**  
      Designed to adapt easily to any Stack Overflow CSV or JSON API dataset format.
    - 🖥️ **Deployment-Ready Architecture**  
      Optimized for Hugging Face Spaces and Streamlit Community Cloud — runs without GPU.
    - 🔄 **Retrainable Pipeline**  
      Full retraining logic included for future model updates using new questions/tags.
    - 🧩 **Modular Codebase**  
      Clean separation of components — text preprocessing, vectorization, model inference, and UI are all modular.
    """)

    st.markdown("---")
    st.success("This project is designed for both practical usage and scalable improvements in production.")
