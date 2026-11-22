import pandas as pd

# Load CSV dataset
df = pd.read_csv("medicine_data.csv")

print("\n========== DATASET INFORMATION ==========")

# Number of rows and columns
print("Dataset Shape:", df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# First 5 records
print("\nFirst 5 Records:")
print(df.head().to_string())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

print("\n========== INSPECTION COMPLETE ==========")
