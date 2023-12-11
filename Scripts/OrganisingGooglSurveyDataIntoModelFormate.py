import csv

# Define the input and output file paths
input_file = "C:\\Users\\Renier\\Desktop\\random\\2021-11-23_polygon.csv"
output_file = "C:\\Users\\Renier\\Desktop\\random\\test.csv"

# Create a dictionary with additional fields
additional_fields = {
    "MAEASaM ID": "",  # Default value for 'MAEASaM ID'
    "Interpretation": 2,  # Index 2 in description
    "Date of imagery": 3,  # Index 3 in description
    "Image type": 4,  # Index 4 in description
    "Interpretation certainty": 5,  # Index 5 in description
    "Survey date": "23-11-2021",
}

# Fields to ignore in the input CSV
ignore_fields = [
    "altitudeMode",
    "timestamp",
    "begin",
    "Name",
    "tessellate",
    "extrude",
    "visibility",
    "drawOrder",
    "description",
    "icon",
    "end",
]

# Open the input and output files
with open(input_file, mode="r", newline="") as infile, open(
    output_file, mode="w", newline=""
) as outfile:
    reader = csv.DictReader(infile)

    # Define the field names for the output CSV
    fieldnames = [
        "WKT",
        "MAEASaM ID",
        "Interpretation",
        "Date of imagery",
        "Image type",
        "Interpretation certainty",
        "Survey date",
    ]

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        # Initialize a new row for the output CSV
        output_row = {}

        # Process and copy fields from the input CSV to the output CSV
        for field in fieldnames:
            if field in additional_fields:
                # Add additional fields from the provided dictionary
                output_row[field] = additional_fields[field]
            elif field not in ignore_fields:
                # Copy fields from the input CSV to the output CSV
                output_row[field] = row.get(
                    field, ""
                )  # Use get to provide a default value ('') when the field is not present

        # Write the modified row to the output CSV
        writer.writerow(output_row)
