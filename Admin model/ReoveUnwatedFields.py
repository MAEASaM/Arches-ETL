import csv

# Input and output file paths
input_file = 'E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\AdminModel.csv'
output_file = 'E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\output_fields.csv'

# Set to keep track of seen IDs
seen_ids = set()

# Open input and output files
with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    
    # Write the header to the output file
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    # Loop through rows in the input file
    for row in reader:
        maeasam_id = row['MAEASaM ID']
        
        # If we haven't seen this ID before, write the entire row
        if maeasam_id not in seen_ids:
            seen_ids.add(maeasam_id)
            writer.writerow(row)
        else:
            # If we have seen this ID before, only write MAEASaM ID, ResourceID, and Geometry columns
            writer.writerow({'MAEASaM ID': maeasam_id, 'ResourceID': row['ResourceID'], 'Geometry': row['Geometry']})
