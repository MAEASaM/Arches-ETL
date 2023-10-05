import sys
import csv
maxInt = sys.maxsize
from shapely import wkt
from shapely.geometry import MultiPolygon, Polygon
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
csv_file = 'E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\AdminModelData.csv'

# Create a dictionary to store the counts of coordinates for each geometry
geometry_counts = defaultdict(int)

# Create a dictionary to store simplified geometries
simplified_geometries = {}

# Set a tolerance value for simplification (adjust as needed)
tolerance = 0.100

# Open the CSV file and read its contents
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Assuming the geometry column is named 'WKT' in your CSV
        geometry_str = row['WKT']  # Replace 'WKT' with the actual column name
        
        # Parse the WKT geometry string
        geometry = wkt.loads(geometry_str)
        
        # Check if the geometry is a MultiPolygon
        if isinstance(geometry, MultiPolygon):
            for polygon in geometry:
                num_coordinates = len(polygon.exterior.coords)
                geometry_id = row['MAEASaM ID']
                geometry_counts[geometry_id] += num_coordinates
                # Simplify the polygon if it has more than 1500 coordinates
                if num_coordinates > 1500:
                    simplified_polygon = polygon.simplify(tolerance, preserve_topology=False)
                    simplified_geometries[geometry_id] = simplified_polygon
        elif isinstance(geometry, Polygon):
            num_coordinates = len(geometry.exterior.coords)
            geometry_id = row['MAEASaM ID']
            geometry_counts[geometry_id] += num_coordinates
            # Simplify the polygon if it has more than 1500 coordinates
            if num_coordinates > 1500:
                simplified_polygon = geometry.simplify(tolerance, preserve_topology=False)
                simplified_geometries[geometry_id] = simplified_polygon

# Check which geometries have more than 1500 coordinates
for geometry_id, count in geometry_counts.items():
    if count > 1500:
        print(f"Geometry with ID '{geometry_id}' has {count} coordinates, which is more than 1500.")

# Access simplified geometries using the 'simplified_geometries' dictionary
for geometry_id, simplified_geometry in simplified_geometries.items():
    # You can do further processing with the simplified geometry, such as saving it to a new CSV or shapefile.
    pass
