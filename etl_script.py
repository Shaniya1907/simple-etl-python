import pandas as pd

# Extract: Read data from CSV
df = pd.read_csv("input_data.csv")

# Transform: Remove duplicates and null values
df_cleaned = df.drop_duplicates().dropna()

# Load: Save cleaned data to a new CSV file
df_cleaned.to_csv("cleaned_data.csv", index=False)

print("ETL Process Completed! Check cleaned_data.csv")