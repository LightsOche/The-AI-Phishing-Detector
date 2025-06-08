# app.py
import streamlit as st
import joblib

# Load trained model and vectorizer
model = joblib.load("model/logistic_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# Label mapping (adjust based on your training labels)
label_map = {
    0: "Safe Email",
    1: "Phishing Email"
}

# Streamlit UI
st.set_page_config(page_title="AI Phishing Detector", layout="centered")
st.title("🔐 AI Phishing Email Detector")
st.markdown("Enter an email text below to check if it's **Safe** or **Phishing**.")

# Input box
email_text = st.text_area("📩 Paste email content here:", height=200)

# Predict button
if st.button("🔍 Detect"):
    if email_text.strip() == "":
        st.warning("Please enter some email content.")
    else:
        transformed_input = vectorizer.transform([email_text])
        prediction = model.predict(transformed_input)[0]

        label = label_map[prediction]

        if label == "Phishing Email":
            st.error("🚨 This is likely a **Phishing Email**!")
        else:
            st.success("✅ This appears to be a **Safe Email**.")
