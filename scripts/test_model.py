# scripts/test_model.py
import joblib

# Load model and vectorizer
model = joblib.load("artifacts/phishing_model.pkl")
vectorizer = joblib.load("artifacts/tfidf_vectorizer.pkl")

def predict_message(msg):
    msg_clean = msg.lower().strip()
    msg_vector = vectorizer.transform([msg_clean])
    prediction = model.predict(msg_vector)[0]
    label = "Phishing" if prediction == 0 else "Legitimate"
    print(f"🔍 Message: {msg}")
    print(f"🛡️ Prediction: {label}")

# Example usage
if __name__ == "__main__":
    msg = input("Enter a message to classify: ")
    predict_message(msg)
