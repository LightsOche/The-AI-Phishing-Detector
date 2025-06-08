import pandas as pd

# Use tab delimiter
df = pd.read_csv('data/phishing_validation_emails.csv', delimiter='\t')

print("📋 Columns:", df.columns)
print("🧾 Sample Data:\n", df.head())
