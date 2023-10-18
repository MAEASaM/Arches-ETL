import csv

input_filename = "E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\output.csv"
output_filename = "E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\AdminModel.csv"


# Open the input CSV file for reading
with open(input_filename, 'r', newline='') as input_file:
    reader = csv.DictReader(input_file)
    
    # Define the field names for the output CSV
    fieldnames = reader.fieldnames
    
    # Open the output CSV file for writing
    with open(output_filename, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        
        # Write the header row to the output CSV
        writer.writeheader()
        
        # Iterate through each row in the input CSV and add the prefix to the "Name" field
        for row in reader:
            if row["Level"] == "0":
                row["Level"] = "Level 0"
            if row["Level"] == "1":
                row["Level"] = "Level 1"
            if row["Level"] == "2":
                row["Level"] = "Level 2"
            # Write the updated row to the output CSV
            writer.writerow(row)