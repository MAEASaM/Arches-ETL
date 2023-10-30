import csv

input_file = "C:\\Users\\Renier\\Desktop\\random\\test1.csv"
output_file = "C:\\Users\\Renier\\Desktop\\random\\test2.csv"


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

        # Generate fieldnames dynamically
        fieldnames = ["WKT"] + [
            f"Description{i+1}" for i in range(max_description_count)
        ]
        csv_file.seek(0)  # Reset the CSV reader to the beginning

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

            csv_writer.writerow(output_row)
    else:
        # Process POINT Z format
        max_description_count = 5  # Define the number of description fields
        fieldnames = ["WKT"] + [
            f"Description{i+1}" for i in range(max_description_count)
        ]
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

            csv_writer.writerow(output_row)
