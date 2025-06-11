# app.py

import streamlit as st
import joblib
import re

# Set page config early
st.set_page_config(page_title="AI Phishing Detector", layout="centered")

# Title
st.title("🔐 AI Phishing Email Detector")
st.markdown("Enter an email text below to check if it's **Safe** or **Phishing**.")

# Load trained model and vectorizer
model = joblib.load("model/logistic_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# Clean text function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\W", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# Label mapping
label_map = {
    0: "Safe Email",
    1: "Phishing Email"
}

# UI input
email_text = st.text_area("📩 Paste email content here:", height=200)

# Predict button
if st.button("🔍 Detect"):
    if email_text.strip() == "":
        st.warning("Please enter some email content.")
    else:
        clean = clean_text(email_text)
        transformed = vectorizer.transform([clean])
        prediction = model.predict(transformed)[0]
        label = label_map[prediction]

        if label == "Phishing Email":
            st.error("🚨 This is likely a **Phishing Email**!")
        else:
            st.success("✅ This appears to be a **Safe Email**.")


