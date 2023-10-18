import json
import pandas as pd
from shapely.geometry import shape, Polygon, MultiPolygon
import csv

# Function to extract and process features from GeoJSON
def extract_features(geojson_file):
    with open(geojson_file, 'r') as file:
        data = json.load(file)

    features = data.get('features', [])
    rows = []

    for feature in features:
        properties = feature.get('properties', {})
        geometry = feature.get('geometry')

        if properties and geometry:
            maeasam_id = properties.get('MAEASaM ID')

            try:
                # Convert the GeoJSON geometry to Shapely shape
                geom = shape(geometry)

                if geom.is_empty:
                    continue

                # Check if it's a MultiPolygon and split it into individual Polygons
                if geom.geom_type == 'MultiPolygon':
                    polygons = [Polygon(poly) for poly in geom.geoms]  # Use geom.geoms
                elif geom.geom_type == 'Polygon':
                    polygons = [geom]
                else:
                    # Unsupported geometry type, store it as a separate row
                    row = {**properties, 'Geometry': None, 'ResourceID': maeasam_id}
                    rows.append(row)
                    continue

                # Create a row for each polygon with the same MAEASaM ID and ResourceID
                for polygon in polygons:
                    row = {**properties, 'Geometry': polygon, 'ResourceID': maeasam_id}
                    rows.append(row)

            except ValueError:
                # Handle other errors if needed
                continue

    df = pd.DataFrame(rows)

    # Sort the DataFrame by 'MAEASaM ID' numerically
    df['Numeric ID'] = df['MAEASaM ID'].str.extract(r'-(\d+)').astype(int)
    df = df.sort_values(by=['MAEASaM ID'])

    # Drop the temporary 'Numeric ID' column
    df = df.drop(columns=['Numeric ID'])

    return df

# Step 1: Extract features and save to a CSV file
geojson_file = 'E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\Admin_model_levels_upload.geojson'
csv_data = extract_features(geojson_file)
csv_data.to_csv('E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\AdminModel.csv', index=False)

# Step 2: Remove duplicate rows based on 'MAEASaM ID' and save to 'output_fields.csv'
input_file = 'E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\AdminModel.csv'
output_file = 'E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\output_fields.csv'

seen_ids = set()

with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        maeasam_id = row['MAEASaM ID']
        if maeasam_id not in seen_ids:
            seen_ids.add(maeasam_id)
            writer.writerow(row)
        else:
            writer.writerow({'MAEASaM ID': maeasam_id, 'ResourceID': row['ResourceID'], 'Geometry': row['Geometry']})

# Step 3: Reorder columns and save the modified DataFrame back to 'AdminModel.csv'
df = pd.read_csv(output_file)
resource_id_column = df['ResourceID']
df.drop(columns=['ResourceID'], inplace=True)

desired_order = ['ResourceID', 'Name Value', 'Name Type', 'MAEASaM ID', 'Official division', 'Level', 'Discription', 'Created At', 'Comment', 'Country', 'Geometry']
df.insert(0, 'ResourceID', resource_id_column)
df = df[desired_order]
df.to_csv(input_file, index=False)