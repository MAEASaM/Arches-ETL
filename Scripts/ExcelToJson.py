import pandas as pd
import json

# Load the Excel file into a Pandas DataFrame
file_path = (
    "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Scripts\\RM thesuarus_new template.xlsx"
)
xls = pd.ExcelFile(file_path)

# Initialize an empty dictionary to hold the JSON data
json_data = {}

# Iterate through each sheet in the Excel file
for sheet_name in xls.sheet_names:
    # Read the sheet into a DataFrame
    df = pd.read_excel(xls, sheet_name, engine="openpyxl")

    # Convert the DataFrame to a list of dictionaries (each row becomes a dictionary)
    sheet_data = df.to_dict(orient="records")

    # Split the sheet name into levels
    levels = sheet_name.split(", ")

    # Create a nested structure in the JSON data
    current_level = json_data
    for level in levels:
        if level not in current_level:
            current_level[level] = {}
        current_level = current_level[level]

    # Assign the sheet data to the current level
    current_level["data"] = sheet_data  # Assign 'data' key to store sheet_data


# Convert the JSON data to a JSON string
json_str = json.dumps(json_data, indent=4)

# Save the JSON string to a file
with open(
    "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Scripts\\output.json", "w"
) as json_file:
    json_file.write(json_str)

print("Excel data converted to JSON successfully.")
