import pandas as pd

def load_data():
    df = pd.read_csv('data/phishing_validation_emails.csv', delimiter='\t')
    
    # Rename for consistency
    df = df.rename(columns={
        'Email Text': 'text',
        'Email Type': 'label'
    })
    
    # Convert labels to binary (1 = phishing, 0 = safe)
    df['label'] = df['label'].apply(lambda x: 1 if x.strip().lower() == 'phishing email' else 0)

    return df
