import os
import joblib  # replace pickle with joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# ✅ Load processed data correctly using joblib
X_train_vec, X_test_vec, y_train, y_test = joblib.load('artifacts/data_processed.pkl')

# Train a Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Make predictions
y_pred = model.predict(X_test_vec)

# Evaluate the model
print("✅ Model training complete.")
print(f"🎯 Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model using joblib
os.makedirs("artifacts", exist_ok=True)
joblib.dump(model, "artifacts/phishing_model.pkl")

print("\n💾 Trained model saved to 'artifacts/phishing_model.pkl'")
