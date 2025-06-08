import pandas as pd

def load_data():
    # Load the new dataset
    data_path = 'data/phishing_validation_emails.csv'
    df = pd.read_csv(data_path)

    # Show basic info
    print("✅ Dataset loaded successfully.")
    print(f"📊 Shape: {df.shape}")
    print(f"🧾 Columns: {list(df.columns)}")
    
    return df
