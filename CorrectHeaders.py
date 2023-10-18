import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Define the path to your input CSV file and required headers with correct capitalization and order
input_csv_file = 'E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\Site_probable_Mali.csv'
required_headers = ['MAEASaM ID', 'Evidence', 'Evidence shape', 'Ground truthed',
                  'Land use land cover', 'Climatic zone', 'Relationship to other site', 'Chronology',
                  'Geometry type', 'Grid level 1', 'Grid level 2', 'Remote sensing activity',
                  'Survey type', 'Survey date', 'Surveyor name', 'Image type', 'Date of imagery',
                  'Spatial resolution (m)', 'Assessment date', 'Assessor name', 'Date of image used',
                  'Overall condition', 'Disturbance effect', 'Extent of impact', 'Severity of impact',
                  'Recommendation for management of disturbance', 'Threat assessor name',
                  'Threat assessment date', 'Image used date', 'Threat type', 'Threat level',
                  'Probability of threat affecting site', 'Recommendation for management of threats',
                  'Measurement type', 'Measurement unit', 'Measurement value'] 

# Define the path to the output CSV file
output_csv_file = 'E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\Site_probable_Mali_corrected.csv'

# Read the input CSV file and get existing headers
existing_headers = []
with open(input_csv_file, 'r') as file:
    reader = csv.reader(file)
    if reader:
        existing_headers = next(reader)  # Get the headers from the first row

# Check for missing headers and headers with incorrect capitalization
missing_headers = [header for header in required_headers if header not in existing_headers]
incorrectly_capitalized = [header for header in existing_headers if header not in required_headers]

# Use fuzzy matching to map incorrect headers to the required headers
header_mapping = {}
for incorrect_header in incorrectly_capitalized:
    matches = process.extract(incorrect_header, required_headers, scorer=fuzz.token_set_ratio)
    best_match, score = max(matches, key=lambda x: x[1])
    if score >= 90:  # You can adjust the threshold as needed
        header_mapping[incorrect_header] = best_match

# Replace incorrectly capitalized headers with the best-matched required headers
for header in header_mapping:
    index = existing_headers.index(header)
    existing_headers[index] = header_mapping[header]

# Reorganize the headers based on the required order, adding any missing required headers
reordered_headers = []
for required_header in required_headers:
    if required_header in existing_headers:
        reordered_headers.append(required_header)
    else:
        reordered_headers.append("")  # Set missing headers to empty string

# Create a dictionary to store the data for each header
data_dict = {header: [] for header in reordered_headers}

# Read the data from the input CSV file and populate the dictionary
with open(input_csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        for header in reordered_headers:
            data_dict[header].append(row.get(header, ''))

# Write the reorganized data to the output CSV file
with open(output_csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(reordered_headers)
    
    for i in range(len(data_dict[reordered_headers[0]])):
        row_data = [data_dict[header][i] for header in reordered_headers]
        writer.writerow(row_data)

print("Missing headers added:", missing_headers)
print("Incorrectly capitalized headers corrected:", incorrectly_capitalized)
print("Headers reordered:", reordered_headers)