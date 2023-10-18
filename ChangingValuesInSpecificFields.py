import csv
import json
from shapely.wkt import loads
from shapely.geometry import mapping

# Input and output file paths
input_csv_file = 'input.csv'
output_geojson_file = 'output.geojson'
mapping_file = 'mapping.json'  # JSON file containing description to field mapping

# Load the mapping from the JSON file and convert keys to lowercase
with open(mapping_file, 'r') as mapping_json:
    mapping_data = json.load(mapping_json)
    description_to_field_mapping = {key.lower(): value for key, value in mapping_data.items()}

# Create a list to store GeoJSON features
geojson_features = []

# Open the input CSV file
with open(input_csv_file, mode='r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        # Initialize the properties dictionary for each row
        properties = {}

        # Extract the 'WKT' column
        wkt = row['WKT']

        # Try to parse the WKT into a Shapely geometry
        try:
            geometry = loads(wkt)
        except Exception as e:
            print(f"Error parsing WKT for row {row}: {str(e)}")
            continue

        # Split the 'description' field and create separate properties
        descriptions = [desc.strip() for desc in row['description'].split(', ')]
        for description in descriptions:
            description_lower = description.lower()
            if description_lower in description_to_field_mapping:
                field_name = description_to_field_mapping[description_lower]
                # Use the mapped field name
                properties[field_name] = row.get(field_name, '')
            else:
                # Manual correction for non-matching values
                manual_correction = input(f"Manual correction needed for '{description}': ")
                # Add the manually corrected value to the corresponding field in the GeoJSON
                properties[manual_correction] = row.get(manual_correction, '')

        properties['geometry'] = mapping(geometry)

        # Create a GeoJSON feature
        feature = {
            "type": "Feature",
            "properties": properties,
            "geometry": mapping(geometry)
        }

        geojson_features.append(feature)

# Create a GeoJSON feature collection
geojson_data = {
    "type": "FeatureCollection",
    "features": geojson_features
}

# Write the GeoJSON data to the output file
with open(output_geojson_file, mode='w', newline='') as geojson_file:
    json.dump(geojson_data, geojson_file, indent=2)

print("GeoJSON file has been created successfully.")