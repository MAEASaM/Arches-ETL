import csv

# Open the input CSV file
with open(
    "C:\\Users\\Renier\\Desktop\\random\\2021-11-23_polygon.csv", "r"
) as input_file:
    csv_reader = csv.reader(input_file)
    header = next(csv_reader)  # Read the header row

    # Find the indices of the "WKT" and "description" columns
    wkt_index = header.index("WKT")
    description_index = header.index("description")

    # Open a new CSV file for writing
    with open(
        "C:\\Users\\Renier\\Desktop\\random\\test1.csv", "w", newline=""
    ) as output_file:
        csv_writer = csv.writer(output_file)

        # Write the header row to the output CSV file
        csv_writer.writerow(["WKT", "description"])

        # Iterate through the input CSV and extract the desired columns
        for row in csv_reader:
            wkt = row[wkt_index]
            description = row[description_index]

            # Write the extracted data to the output CSV file
            csv_writer.writerow([wkt, description])
