import pandas as pd

# Define the file path
file_path = "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\zim_modified.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows that contain only null values
df = df.dropna(how='all')

# Save the modified DataFrame to a new CSV file
modified_file_path = "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\zim_modified_no_null.csv"
df.to_csv(modified_file_path, index=False)

print(f"Modified CSV file saved to: {modified_file_path}")
