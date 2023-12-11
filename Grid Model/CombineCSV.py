import pandas as pd

# Read the input CSV files
file1 = pd.read_csv(
    "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\Grid\\Grid level 1_ArchesUpload.csv"
)
file2 = pd.read_csv(
    "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\Grid\\Grid level 2_ArchesUpload.csv"
)

# Concatenate the data from both files
combined_data = pd.concat([file1, file2])

# Extract the numeric part from the 'Resource ID' column
combined_data["NumericPart"] = combined_data["Resource ID"].str.extract("(\d+)$")

# Convert the 'NumericPart' column to numeric for correct sorting
combined_data["NumericPart"] = pd.to_numeric(combined_data["NumericPart"])

# Sort the data based on the 'MAEASaM ID' column and the numeric part of 'Resource ID'
combined_data = combined_data.sort_values(["MAEASaM ID", "NumericPart"])

# Drop the temporary columns used for sorting
combined_data = combined_data.drop(columns=["NumericPart"])

# Write the organized data to a new CSV file
combined_data.to_csv(
    "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\Grid\\result.csv",
    index=False,
)
