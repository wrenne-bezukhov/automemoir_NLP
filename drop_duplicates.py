import pandas as pd

# Load your CSV file into a pandas DataFrame
df = pd.read_csv('les_annees_run_results_eng.csv') 

# Remove duplicate rows
cleaned_df = df.drop_duplicates()

# Save the cleaned DataFrame to a new CSV file
cleaned_df.to_csv('les_annees_run_results_no_duplicates.csv', index=False)

