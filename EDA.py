import streamlit as st
import pandas as pd
import ast
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

def run_EDA(df):
    st.set_page_config(page_title="Stack Overflow EDA", layout="wide")
    st.title("📊 Stack Overflow Tag Prediction - EDA")

    # Clean tags column if needed
    df["Tags"] = df["Tags"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

    # Show raw data
    st.subheader("📄 Raw Dataset")
    st.dataframe(df.head(10))

    # Basic stats
    st.subheader("📌 Basic Information")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Number of Rows:**", df.shape[0])
        st.write("**Number of Columns:**", df.shape[1])
    with col2:
        st.write("**Missing Values per Column:**")
        st.dataframe(df.isnull().sum())

    # Number of tags per question
    st.subheader("🔢 Tags per Question")
    df["num_tags"] = df["Tags"].apply(len)
    fig1, ax1 = plt.subplots()
    sns.histplot(df["num_tags"], bins=range(1, 10), kde=False, ax=ax1)
    ax1.set_xlabel("Number of Tags")
    ax1.set_ylabel("Number of Questions")
    st.pyplot(fig1)

    # Most common tags
    st.subheader("🏷️ Most Common Tags")
    all_tags = [tag for tags in df["Tags"] for tag in tags]
    tag_counts = Counter(all_tags)
    most_common = tag_counts.most_common(20)
    common_df = pd.DataFrame(most_common, columns=["Tag", "Count"])

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.barplot(data=common_df, x="Count", y="Tag", palette="Blues_r", ax=ax2)
    st.pyplot(fig2)

    # Tag frequency table
    with st.expander("📊 Full Tag Frequency Table"):
        tag_freq_df = pd.DataFrame(tag_counts.items(), columns=["Tag", "Count"]).sort_values(by="Count", ascending=False)
        st.dataframe(tag_freq_df)

    # Length of questions
    st.subheader("✏️ Question Length Distribution")
    df["char_count"] = df["Body"].astype(str).apply(len)
    fig3, ax3 = plt.subplots()
    sns.histplot(df["char_count"], bins=50, kde=True, ax=ax3)
    ax3.set_xlabel("Character Count")
    ax3.set_ylabel("Number of Questions")
    st.pyplot(fig3)

    # Word count
    st.subheader("📚 Word Count Distribution")
    df["word_count"] = df["Body"].astype(str).apply(lambda x: len(x.split()))
    fig4, ax4 = plt.subplots()
    sns.boxplot(x=df["word_count"], ax=ax4)
    ax4.set_xlabel("Word Count per Question")
    st.pyplot(fig4)

    # Filter by tag
    st.subheader("🔍 Filter Questions by Tag")
    selected_tag = st.selectbox("Choose a tag to see related questions", sorted(tag_freq_df["Tag"].tolist()))
    filtered_df = df[df["Tags"].apply(lambda tags: selected_tag in tags)]

    st.write(f"Showing {len(filtered_df)} questions tagged with **{selected_tag}**:")
    st.dataframe(filtered_df[["Body", "Tags"]].head(10))
