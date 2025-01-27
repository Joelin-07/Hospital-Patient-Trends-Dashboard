import pandas as pd

# Load the dataset
data_path = "synthetic_hospital_data.csv" 
df = pd.read_csv(data_path)

# Clean the dataset

# Remove duplicates
df_cleaned = df.drop_duplicates()

# Handle missing values
df_cleaned['Age'].fillna(df_cleaned['Age'].median(), inplace=True)
df_cleaned['LengthOfStay'].fillna(df_cleaned['LengthOfStay'].median(), inplace=True)

# Perform basic statistical analysis

# Calculate statistics
mean_age = df_cleaned['Age'].mean()
median_age = df_cleaned['Age'].median()
std_age = df_cleaned['Age'].std()

mean_length_of_stay = df_cleaned['LengthOfStay'].mean()
median_length_of_stay = df_cleaned['LengthOfStay'].median()
std_length_of_stay = df_cleaned['LengthOfStay'].std()

# Create a summary table
summary_table = {
    "Metric": ["Mean Age", "Median Age", "Std Dev Age", "Mean Length of Stay", "Median Length of Stay", "Std Dev Length of Stay"],
    "Value": [
        mean_age, median_age, std_age,
        mean_length_of_stay, median_length_of_stay, std_length_of_stay
    ]
}
summary_df = pd.DataFrame(summary_table)

# Save the cleaned dataset and summary table
cleaned_data_path = "cleaned_hospital_data.csv"
summary_data_path = "summary_statistics.csv"
df_cleaned.to_csv(cleaned_data_path, index=False)
summary_df.to_csv(summary_data_path, index=False)

print(f"Cleaned dataset saved to: {cleaned_data_path}")
print(f"Summary statistics saved to: {summary_data_path}")
