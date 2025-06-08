# train_model.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score

from load_data import load_data

# Load and clean data
X, y = load_data()
df = pd.DataFrame({'Email Text': X, 'Email Type': y})
df = df.dropna()
X = df['Email Text']
y = df['Email Type']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Evaluate
y_pred = model.predict(X_test_vec)
print("✅ Model training complete.")
print(f"🎯 Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print("📊 Classification Report:\n")
print(classification_report(y_test, y_pred))

# Save model and vectorizer
joblib.dump(model, "model/logistic_model.pkl")
joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")
print("💾 Model and vectorizer saved to 'model/' directory.")
