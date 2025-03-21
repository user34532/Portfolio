import pandas as pd

# Simulated data extraction from Supermetrics
data = {
    'campaign': ['Ad1', 'Ad2', 'Ad3'],
    'clicks': [100, 250, 175],
    'impressions': [1000, 5000, 3000]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('supermetrics_data.csv', index=False)
print("Supermetrics data saved successfully!")
