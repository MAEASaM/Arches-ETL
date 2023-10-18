import pandas as pd
import re

# Read the CSV file
input_csv_file = 'zim_modified.csv'
df = pd.read_csv(input_csv_file)

point_pattern = re.compile(r'POINT Z', re.IGNORECASE)
polygon_pattern = re.compile(r'POLYGON Z', re.IGNORECASE)
linestring_pattern = re.compile(r'LINESTRING Z', re.IGNORECASE)

# Create separate DataFrames for each geometry type
point_df = df[df['WKT'].str.contains(point_pattern)]
polygon_df = df[df['WKT'].str.contains(polygon_pattern)]
linestring_df = df[df['WKT'].str.contains(linestring_pattern)]

point_output_file = 'output_POINT_Z.csv'
polygon_output_file = 'output_POLYGON_Z.csv'
linestring_output_file = 'output_LINESTRING_Z.csv'

# Save DataFrames to separate CSV files
point_df.to_csv(point_output_file, index=False)
polygon_df.to_csv(polygon_output_file, index=False)
linestring_df.to_csv(linestring_output_file, index=False)