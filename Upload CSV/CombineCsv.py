import os
import pandas as pd

# Specify the folder where your CSV files are located
folder_path = "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\Upload CSV"

# Get a list of all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

# Initialize an empty list to store the DataFrames
dataframes = []

# Iterate through each CSV file and append its data to the list
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Concatenate all DataFrames into one
combined_data = pd.concat(dataframes, ignore_index=True)

# Sort the combined data based on a specific column containing entries like "RS-SDN-00000029"
combined_data.sort_values(by="ResourceID", inplace=True)

# Reset the index to have a numerical sequence intact
combined_data.reset_index(drop=True, inplace=True)

# Specify the output file where you want to save the combined data
output_file = "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\Upload CSV\\combined.csv"

# Save the combined data to a new CSV file
combined_data.to_csv(output_file, index=False)

print(f"Combined data saved to {output_file}")
