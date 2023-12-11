import pandas as pd

# Read the input CSV file
input_file = "C:\\Users\\Renier\\Desktop\\random\\test2.csv"
input_df = pd.read_csv(input_file)

# Create a mapping of the fields you want to copy from input to output
field_mapping = {
    "Description1": "Interpretation",
    "Description2": "Date of imagery",
    "Description3": "Image type",
    "Description4": "Interpretation certainty",
    "Description5": "Additional information",
}

# Add the remaining column names to the list
output_columns = [
    "WKT",
    "Year",
    "MAEASaM ID",
    "Evidence",
    "Evidence shape",
    "Ground truthed",
    "Land use land cover",
    "Climatic zone",
    "Relationship to other site",
    "Chronology",
    "Geometry type",
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

# Create the output DataFrame with all columns and fill with default values
output_df = pd.DataFrame(columns=output_columns)

# Match WKT to Geometry
output_df["Geometry type"] = input_df["WKT"]

# Merge specified fields by splitting the values
for field in field_mapping:
    input_values = input_df[field].str.split(",").str.get(0)
    output_df[field_mapping[field]] = input_values

# Fill the remaining columns with default values
output_df.fillna("", inplace=True)

# Save the output CSV
output_file = "C:\\Users\\Renier\\Desktop\\random\\test3.csv"
output_df.to_csv(output_file, index=False)
