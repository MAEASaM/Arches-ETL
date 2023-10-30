import csv

input_file = "C:\\Users\\Renier\\Desktop\\random\\Botswana — 2021-10-19_point.csv"
output_file = (
    "C:\\Users\\Renier\\Desktop\\random\\split\\Botswana — 2021-10-19_point.csv"
)

# Define the additional fieldnames
additional_fieldnames = [
    "MAEASaM ID",
    "Evidence",
    "Evidence shape",
    "Interpretation",
    "Interpretation certainty",
    "Ground truthed",
    "Land use land cover",
    "Climatic zone",
    "Relationship to other site",
    "Chronology",
    "Geometry type",
    "Grid level 1",
    "Grid level 2",
    "Remote sensing activity",
    "Survey type",
    "Survey date",
    "Surveyor name",
    "Image type",
    "Date of imagery",
    "Spatial resolution (m)",
    "Assessment date",
    "Assessor name",
    "Date of image used",
    "Overall condition",
    "Disturbance effect",
    "Extent of impact",
    "Severity of impact",
    "Recommendation for management of disturbance",
    "Threat assessor name",
    "Threat assessment date",
    "Image used date",
    "Threat type",
    "Threat level",
    "Probability of threat affecting site",
    "Recommendation for management of threats",
    "Measurement type",
    "Measurement unit",
    "Measurement value",
]


def is_polygon_format(header):
    return "altitudeMode" in header


# Open the input and output CSV files
with open(input_file, mode="r") as csv_file, open(
    output_file, mode="w", newline=""
) as output_csv:
    csv_reader = csv.DictReader(csv_file)
    header = csv_reader.fieldnames

    if is_polygon_format(header):
        # Process POLYGON Z format
        max_description_count = 0

        for row in csv_reader:
            description = row["description"]
            descriptions = [desc.strip() for desc in description.split(",")]
            max_description_count = max(max_description_count, len(descriptions))

        # Generate fieldnames dynamically, including the additional ones
        fieldnames = (
            ["WKT"]
            + [f"Description{i+1}" for i in range(max_description_count)]
            + additional_fieldnames
        )

        # Reset the CSV reader to the beginning
        csv_file.seek(0)
        next(csv_reader)  # Skip the first row

        csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in csv_reader:
            wkt = row["WKT"]
            description = row["description"]
            descriptions = [desc.strip() for desc in description.split(",")]
            descriptions = descriptions + [""] * (
                max_description_count - len(descriptions)
            )

            output_row = {"WKT": wkt}
            for i, desc in enumerate(descriptions):
                output_row[f"Description{i+1}"] = desc
            # Add empty values for the additional fields
            for field in additional_fieldnames:
                output_row[field] = ""

            csv_writer.writerow(output_row)
    else:
        # Process the first script logic when it's not a POLYGON Z format
        fieldnames = ["WKT", "description"] + additional_fieldnames
        csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        csv_writer.writeheader()

        # Reset the CSV reader to the beginning
        csv_file.seek(0)
        next(csv_reader)  # Skip the first row

        for row in csv_reader:
            wkt = row["WKT"]
            description = row["description"]
            # Create an output row dictionary with empty values for additional fields
            output_row = {"WKT": wkt, "description": description}
            for field in additional_fieldnames:
                output_row[field] = ""
            csv_writer.writerow(output_row)
