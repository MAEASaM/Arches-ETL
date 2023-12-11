import pandas as pd

# Replace 'file1.csv' and 'file2.csv' with the actual paths to your CSV files
file1_path = "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Kenya_Angela_polygon_corrected.csv"
file2_path = (
    "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Kenya_Angela_point_corrected.csv"
)

# Read the CSV files into pandas DataFrames without any data type conversions
df1 = pd.read_csv(file1_path, dtype=str)
df2 = pd.read_csv(file2_path, dtype=str)

# Concatenate the DataFrames along the rows (axis=0)
combined_df = pd.concat([df1, df2], ignore_index=True)

# Replace 'combined_file.csv' with the desired name for the new CSV file
combined_df.to_csv(
    "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\KenyaAngelaCombined.csv",
    index=False,
)
