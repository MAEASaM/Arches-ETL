import csv
import json
from shapely.wkt import loads
from shapely.geometry import mapping

# Input and output file paths
input_csv_file = "C:\\Users\\Renier\\Desktop\\random\\Botswana — 2021-11-23_poly.csv"
output_geojson_file = (
    "C:\\Users\\Renier\\Desktop\\random\\split\\Botswana — 2021-11-23_poly.geojson"
)


# Define the fieldnames for additional attributes
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
    "Spatial resolution m",
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


# Create a list to store GeoJSON features
geojson_features = []

# Open the input CSV file
with open(input_csv_file, mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        # Initialize the properties dictionary for each row
        properties = {}

        # Extract the 'WKT' column
        wkt = row["WKT"]

        # Try to parse the WKT into a Shapely geometry
        try:
            geometry = loads(wkt)
        except Exception as e:
            print(f"Error parsing WKT for row {row}: {str(e)}")
            continue

        # Split the 'description' field and create separate properties
        descriptions = [desc.strip() for desc in row["description"].split(", ")]
        for i, description in enumerate(descriptions):
            properties[
                f"Description{i + 1}"
            ] = description  # Create separate properties for each value

        # Remove the 'description' field
        if "description" in row:
            del row["description"]

        properties["geometry"] = mapping(geometry)

        # Add the additional fields to the GeoJSON properties
        for field in additional_fieldnames:
            properties[field] = row.get(field, "")

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
with open(output_geojson_file, mode="w") as geojson_file:
    json.dump(geojson_data, geojson_file, indent=2)

print("GeoJSON file has been created successfully.")
