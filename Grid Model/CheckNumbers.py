import pandas as pd

# Load the CSV file into a DataFrame
file_path = "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\Grid\\Grid level 2.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Create a new column called "Resource ID" and copy values from "MAEASaM ID"
df["Resource ID"] = df["MAEASaM ID"]

# Save the updated DataFrame to a new CSV file
output_file_path = "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\Grid\\Grid level 2_ArchesUpload.csv"  # Replace with the desired output file path
df.to_csv(output_file_path, index=False)

print(f"Script executed successfully. Output saved to {output_file_path}")
