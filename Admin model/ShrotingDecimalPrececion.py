
import csv

# Function to round coordinates to 5 decimal places
def round_coordinates(coords):
    try:
        return [(round(float(coord), 5)) for coord in coords.split()]
    except ValueError:
        return coords  # Return the original value if it's not numeric

# Input and output file paths
input_file = 'E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\AdminModel.csv'
output_file = 'E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\AdminModelShort.csv'

# Open input and output CSV files
with open(input_file, mode='r') as csv_input, open(output_file, mode='w', newline='') as csv_output:
    reader = csv.reader(csv_input)
    writer = csv.writer(csv_output)

    # Process header row
    header = next(reader)
    writer.writerow(header)

    # Process data rows
    for row in reader:
        # Assuming the 'WKT' field is in the second column (index 1)
        wkt_field = row[1]

        # Round the coordinates in the 'WKT' field
        rounded_wkt = ' '.join(map(str, round_coordinates(wkt_field)))
        
        # Replace the 'WKT' field with rounded coordinates
        row[1] = rounded_wkt

        # Write the updated row to the output CSV
        writer.writerow(row)

print("CSV file with rounded coordinates saved as", output_file)