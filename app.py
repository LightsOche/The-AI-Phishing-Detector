import streamlit as st
import joblib
import re

# Load model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\W", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# Prediction function
def predict_email(email):
    clean = clean_text(email)
    vector = vectorizer.transform([clean])
    prediction = model.predict(vector)
    return "Phishing Email" if prediction[0] == 1 else "Safe Email"

# Streamlit UI
st.title("AI Phishing Email Detector")
st.write("Paste an email below to check if it's phishing or not.")

email_input = st.text_area("Email Content", height=200)

if st.button("Analyze"):
    if email_input.strip():
        result = predict_email(email_input)
        st.success(f"Result: {result}")
    else:
        st.warning("Please enter some email text.")
