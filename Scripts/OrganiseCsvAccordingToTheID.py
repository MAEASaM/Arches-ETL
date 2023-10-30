import csv

# Define the input and output file paths
input_file_path = "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\MaliGeomCorrected.csv"
output_file_path = "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\MaliGeomCorrectedSorted.csv"

# Initialize fieldnames as an empty list
fieldnames = []

# Initialize a list to hold the data rows
data_rows = []

# Read the input CSV file
with open(input_file_path, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.reader(file)

    # Read each row
    for row in reader:
        if not fieldnames:
            # If fieldnames is empty, this is the header row
            fieldnames = row
        else:
            # This is a data row
            data_rows.append(row)

# Create a dictionary to map original IDs to new IDs
id_mapping = {}
next_id = 1

# Find the index of the "MAEASaM ID" field using fieldnames
id_index = fieldnames.index("MAEASaM ID")

# Modify the "MAEASaM ID" field values and update the mapping
for i, row in enumerate(data_rows):
    original_id = row[id_index]

    new_id = f"RS-MLI-{next_id:08d}"
    id_mapping[original_id] = new_id
    data_rows[i][id_index] = new_id
    next_id += 1

# Sort the data rows based on the modified "MAEASaM ID"
sorted_data_rows = sorted(data_rows, key=lambda row: row[id_index])

# Write the modified data back to a new CSV file with the same header
with open(output_file_path, "w", newline="") as new_file:
    writer = csv.writer(new_file)

    # Write the fieldnames as the first row
    writer.writerow(fieldnames)

    # Write the sorted data rows
    writer.writerows(sorted_data_rows)
