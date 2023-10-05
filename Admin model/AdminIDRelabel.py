import sys
import csv
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
        
# Read the CSV file
with open('E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\AdminModelData.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# Create a dictionary to map country names to country codes
country_codes = {
    'Botswana': 'BWA',
    'Ethiopia': 'ETH',
    'Kenya': 'KEN',
    'Mali': 'MLI',
    'Senegal': 'SEN',
    'Sudan': 'SDN',
    'Tanzania': 'TZA',
    'Zimbabwe': 'ZWE',
    'Africa': 'AFR'
}

# Create a dictionary to keep track of the counts for each country
country_counts = {}

# Sort the rows by Country and Level
sorted_rows = sorted(rows, key=lambda x: (x['Country'], x['Level']))

# Iterate through the sorted rows and generate unique IDs
for row in sorted_rows:
    country = row['Country']
    
    if country not in country_counts:
        country_counts[country] = 1
    else:
        country_counts[country] += 1
    
    # Calculate the numeric part of the ID
    numeric_part = str(country_counts[country]).zfill(7)
    
    # Get the country code based on the country name
    country_code = country_codes.get(country, 'XXX')  # 'XXX' is a placeholder if the country code is not found
    
    # Create the unique ID
    unique_id = f"ADMN-{country_code}-{numeric_part}"
    
    # Update the 'MAEASaM ID' column in the row
    row['MAEASaM ID'] = unique_id
    
    # Set the 'ResourceID' column to match 'MAEASaM ID' without the 'RESOURCE-' prefix
    row['ResourceID'] = unique_id.replace('RESOURCE-', '')

# Write the updated data back to a new CSV file
with open('E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\AdminModel.csv', 'w', newline='') as csvfile:
    fieldnames = reader.fieldnames + ['ResourceID']  # Add 'ResourceID' to the fieldnames
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sorted_rows)