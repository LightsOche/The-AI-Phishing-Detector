# scripts/load_data.py
import pandas as pd

def load_data():
    df = pd.read_csv("data/phishing_data.csv")
    print("Data loaded successfully. Here's a preview:")
    print(df.head())

if __name__ == "__main__":
    load_data()
