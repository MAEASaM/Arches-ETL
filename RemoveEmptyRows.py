import csv

with open('E:\\MAEASaM\\MAEASaM_desktop\\Arches\Arches Git\\Arches-ETL\\Sudan_modified.csv', 'r', newline='') as input_file, open('E:\\MAEASaM\\MAEASaM_desktop\\Arches\Arches Git\\Arches-ETL\\SudanModified.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    for row in reader:
        # Check if the row is empty (all fields are empty or whitespace)
        if any(field.strip() for field in row):
            writer.writerow(row)

input_file.close()
output_file.close()