import pandas as pd

# Load memory recall dataset
df = pd.read_csv('memory_data.csv')

# Process data (example: filtering invalid responses)
df_clean = df.dropna()

# Save cleaned data
df_clean.to_csv('cleaned_memory_data.csv', index=False)
print("Memory recall data processed successfully!")
