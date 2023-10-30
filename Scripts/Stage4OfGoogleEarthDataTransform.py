import csv
import pandas as pd

# Define the input and output file names
input_file = "C:\\Users\\Renier\\Desktop\\random\\2021-11-23_polygon.csv"
output_file = "C:\\Users\\Renier\\Desktop\\random\\test3.csv"

# Open the input CSV file
with open(input_file, "r") as input_csv:
    csv_reader = csv.reader(input_csv)
    header = next(csv_reader)  # Read the header row

    # Find the indices of the "WKT" and "description" columns
    wkt_index = header.index("WKT")
    description_index = header.index("description")

    # Initialize a list to store the rows with extracted and newly created fields
    output_data = []

    for row in csv_reader:
        wkt = row[wkt_index]
        description = row[description_index]

        # Split the "description" field by commas and strip any leading/trailing whitespace
        descriptions = [desc.strip() for desc in description.split(",")]

        # Create new fields for up to 4 descriptions (adjust the number as needed)
        for i in range(5):
            row.append(descriptions[i] if i < len(descriptions) else "")

        # Append the row to the output data
        output_data.append(row)

# Define the desired field names for the output CSV in the required order
desired_fields = [
    "WKT",
    "Interpretation",
    "Date of imagery",
    "Image type",
    "Interpretation certainty",
    "Additional information",
]

# Reorder the columns based on the desired order
output_data = [
    [row[header.index(field)] for field in desired_fields] for row in output_data
]

# Open the output CSV file for writing
with open(output_file, "w", newline="") as output_csv:
    csv_writer = csv.writer(output_csv)

    # Write the header row with the desired fields
    csv_writer.writerow(desired_fields)

    # Write the selected rows to the output CSV file
    csv_writer.writerows(output_data)
