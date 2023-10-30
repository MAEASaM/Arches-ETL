import csv
import json
from shapely.wkt import loads
from shapely.geometry import mapping

# Input and output file paths
input_csv_file = "C:\\Users\\Renier\\Desktop\\random\\Botswana — 2021-11-23_poly.csv"
output_geojson_file = (
    "C:\\Users\\Renier\\Desktop\\random\\split\\Botswana — 2021-11-23_poly_test.geojson"
)

additional_fieldnames = [
    "MAEASaM ID",
    "Evidence",
    "Evidence shape",
    "Interpretation",
    "Interpretation certainty",
    "Ground truthed",
    "Land use land cover",
    "Climatic zone",
    "Relationship to other site",
    "Chronology",
    "Grid level 1",
    "Grid level 2",
    "Remote sensing activity",
    "Survey type",
    "Survey date",
    "Surveyor name",
    "Image type",
    "Date of imagery",
    "Spatial resolution (m)",
    "Assessment date",
    "Assessor name",
    "Date of image used",
    "Overall condition",
    "Disturbance effect",
    "Extent of impact",
    "Severity of impact",
    "Recommendation for management of disturbance",
    "Threat assessor name",
    "Threat assessment date",
    "Image used date",
    "Threat type",
    "Threat level",
    "Probability of threat affecting site",
    "Recommendation for management of threats",
    "Measurement type",
    "Measurement unit",
    "Measurement value",
]

# Load the mapping from the JSON file and convert keys to lowercase
mapping_file = "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Scripts\\collections_mapping.json"  # JSON file containing description to field mapping
with open(mapping_file, "r") as mapping_json:
    mapping_data = json.load(mapping_json)
    description_to_field_mapping = {
        key.lower(): value for key, value in mapping_data.items()
    }

geojson_features = []

# Open the input CSV file
with open(input_csv_file, mode="r", newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        # Create an empty 'properties' dictionary with all the additional field names
        properties = {field: None for field in additional_fieldnames}

        # Split the 'description' field and map its values to the corresponding fields
        descriptions = [desc.strip() for desc in row["description"].split(", ")]
        for description in descriptions:
            # Lowercase the description for case-insensitive matching
            description_lower = description.lower()
            if description_lower in description_to_field_mapping:
                field_name = description_to_field_mapping[description_lower]
                properties[field_name] = description

        # Extract the 'WKT' column
        wkt = row["WKT"]

        # Try to parse the WKT into a Shapely geometry
        try:
            geometry = loads(wkt)
        except Exception as e:
            print(f"Error parsing WKT for row {row}: {str(e)}")
            continue

        properties["geometry"] = mapping(geometry)

        # Create a GeoJSON feature
        feature = {
            "type": "Feature",
            "properties": properties,
            "geometry": mapping(geometry),
        }

        geojson_features.append(feature)

# Create a GeoJSON feature collection
geojson_data = {"type": "FeatureCollection", "features": geojson_features}

# Write the GeoJSON data to the output file
with open(output_geojson_file, mode="w", newline="") as geojson_file:
    json.dump(geojson_data, geojson_file, indent=2)

print("GeoJSON file has been created successfully.")
