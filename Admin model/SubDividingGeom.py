import pandas as pd
import re
import sys
import csv
from shapely.geometry import MultiPolygon
from collections import defaultdict

# Increase the maxInt value to avoid OverflowError
maxInt = sys.maxsize
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)

# Read the CSV file into a DataFrame
df = pd.read_csv(r'E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\DividTest.csv')

# Define a function to parse the coordinates from the "Geometry" column
def parse_coordinates(geometry_str):
    # Use regular expression to extract coordinates
    coordinates = re.findall(r'(\d+\.\d+) (-\d+\.\d+)', geometry_str)
    return [(float(lon), float(lat)) for lon, lat in coordinates]

# Define a function to find the two outermost coordinates on a straight line
def find_outermost_coordinates(coordinates):
    if not coordinates:
        # Handle the case where coordinates is empty
        return None, None

    min_x = min(coordinates, key=lambda x: x[0])
    max_x = max(coordinates, key=lambda x: x[0])
    min_y = min(coordinates, key=lambda x: x[1])
    max_y = max(coordinates, key=lambda x: x[1])

    return (min_x, min_y), (max_x, max_y)

# Iterate through the DataFrame
for index, row in df.iterrows():
    # Parse the coordinates
    coordinates = parse_coordinates(row['Geometry'])

    # Find the outermost coordinates on the straight line
    min_coord, max_coord = find_outermost_coordinates(coordinates)

    # Remove coordinates between min_coord and max_coord
    coordinates = [coord for coord in coordinates if coord == min_coord or coord == max_coord or not (min_coord[0] <= coord[0] <= max_coord[0])]

    # Convert the coordinates back to the geometry string format
    new_geometry = ' '.join([f'{lon} {lat}' for lon, lat in coordinates])

    # Update the DataFrame with the new geometry
    df.at[index, 'Geometry'] = f'MultiPolygon ((({new_geometry})))'

# Save the updated DataFrame to a new CSV file
df.to_csv(r'updated_csv_file.csv', index=False)