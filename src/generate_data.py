import pandas as pd
import numpy as np
import os

def generate_synthetic_data(num_samples=1000):
    np.random.seed(42)
    
    # Features
    document_length = np.random.normal(loc=5000, scale=1500, size=num_samples).astype(int)
    document_length = np.clip(document_length, 500, 15000)
    
    num_claims = np.random.poisson(lam=15, size=num_samples)
    num_claims = np.clip(num_claims, 1, 100)
    
    filing_type = np.random.choice(['Patent', 'Trademark', 'Copyright', 'Design'], size=num_samples, p=[0.5, 0.3, 0.1, 0.1])
    
    template_complexity = np.random.choice(['Low', 'Medium', 'High'], size=num_samples, p=[0.2, 0.5, 0.3])
    
    historical_success_rate = np.random.uniform(low=0.3, high=0.95, size=num_samples)
    
    # Generate Target Variable based on some arbitrary rules to make the ML model learn something
    approval_prob = np.zeros(num_samples)
    
    # Patents are harder, Trademarks are easier
    approval_prob += np.where(filing_type == 'Patent', -0.1, 0.1)
    approval_prob += np.where(filing_type == 'Trademark', 0.2, 0.0)
    
    # More claims generally lower probability if too many
    approval_prob -= (num_claims / 100.0) * 0.2
    
    # Higher historical success rate increases probability
    approval_prob += historical_success_rate * 0.5
    
    # High complexity might decrease probability if too long
    approval_prob -= np.where((template_complexity == 'High') & (document_length > 8000), 0.2, 0)
    
    # Normalize probabilities and add noise
    approval_prob += np.random.normal(0, 0.1, num_samples)
    approval_prob = np.clip(approval_prob, 0.05, 0.95)
    
    # Binary Target
    is_approved = (np.random.rand(num_samples) < approval_prob).astype(int)
    
    df = pd.DataFrame({
        'document_length': document_length,
        'num_claims': num_claims,
        'filing_type': filing_type,
        'template_complexity': template_complexity,
        'historical_success_rate': historical_success_rate,
        'is_approved': is_approved
    })
    
    return df

if __name__ == '__main__':
    print("Generating synthetic data for Intellectual Property Filings...")
    df = generate_synthetic_data(1500)
    
    # Ensure data directory exists
    os.makedirs('../data', exist_ok=True)
    
    file_path = '../data/ip_filings_synthetic_data.csv'
    df.to_csv(file_path, index=False)
    print(f"Data successfully generated and saved to {file_path}")
    print(df.head())
    print(f"Class distribution:\n{df['is_approved'].value_counts(normalize=True)}")
