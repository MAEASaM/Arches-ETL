import json
import pandas as pd
from shapely.geometry import shape, Polygon, MultiPolygon

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
                    row = {**properties, 'Geometry': None}
                    rows.append(row)
                    continue

                # Create a row for each polygon with the same MAEASaM ID
                for polygon in polygons:
                    row = {**properties, 'Geometry': polygon}
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

# Usage: Specify your GeoJSON file path here
geojson_file = 'E:\MAEASaM\MAEASaM_desktop\Arches\Admin Resource Model\Finale files\Admin_model_levels_upload.geojson'
csv_data = extract_features(geojson_file)

# Save the resulting DataFrame to a CSV file
csv_file = 'E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\AdminModel.csv'
csv_data.to_csv(csv_file, index=False)
