import sys
import csv
maxInt = sys.maxsize
from shapely import wkt
from collections import defaultdict

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

# Specify the CSV file name
csv_file = 'E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\DividTest.csv'

# Create a dictionary to store the counts of coordinates for each geometry
geometry_counts = defaultdict(int)

# Open the CSV file and read its contents
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Assuming the geometry column is named 'WKT' in your CSV
        geometry_str = row['WKT']  # Replace 'WKT' with the actual column name
        
        # Parse the WKT geometry string
        geometry = wkt.loads(geometry_str)
        
        # Check if the geometry is a MultiPolygon
        if geometry.geom_type == 'MultiPolygon':
            # Iterate through individual polygons within the MultiPolygon
            for polygon in geometry:
                num_coordinates = len(polygon.exterior.coords)
                # Update the count for the geometry
                geometry_counts[row['id']] += num_coordinates
        else:
            num_coordinates = len(geometry.exterior.coords)
            # Update the count for the geometry
            geometry_counts[row['MAEASaM ID']] += num_coordinates

# Check which geometries have more than 1500 coordinates
for geometry_id, count in geometry_counts.items():
    if count > 1500:
        print(f"Geometry with ID '{geometry_id}' has {count} coordinates, which is more than 1500.")
