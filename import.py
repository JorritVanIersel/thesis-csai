import os
import pandas as pd

# Load the CSV file with the correct encoding and specify headers
file_path = 'texts_2024_1120_aggregate.csv'

# Define the headers
headers = ['fullname', 'Measures', 'Amount', 'Level', 'Function']  # Replace with your actual headers

df = pd.read_csv(file_path, encoding='latin1', names=headers, header=0)
df['filename'] = df['fullname'].str.split('/').str[-1]

# Extract type, id, and model
df[['type', 'id', 'model']] = df['filename'].str.extract(r'(\w+)_(\d+)@(\w+)')

# Group by type and model
grouped = df.groupby(['type', 'model'])

# Calculate the mean for each feature in the group
mean_features = grouped.mean()

# Print the results
print(mean_features)