import os
from qgis.core import QgsVectorLayer, QgsFeature, QgsGeometry, QgsField, QgsVectorFileWriter, QgsProject

# Input and output file paths
input_file = "path/to/your/input/polygon.shp"
output_file = "path/to/your/output/polygon_combined.shp"

# Define the maximum number of coordinates in each segment
max_coordinates_per_segment = 1400

# Load the input vector layer
layer = QgsVectorLayer(input_file, "input_layer", "ogr")

# Check if the layer was loaded successfully
if not layer.isValid():
    print("Error: Could not load the input layer.")
else:
    # Create a new memory layer for the combined features
    combined_layer = QgsVectorLayer("Polygon?crs=" + layer.crs().authid(), "combined_layer", "memory")
    provider = combined_layer.dataProvider()
    fields = layer.fields()

    # Iterate through features in the input layer
    for feature in layer.getFeatures():
        geom = feature.geometry()

        # Handle MultiPolygon geometries
        if geom.isMultipart():
            for part in geom.asMultiPolygon():
                coordinates = part[0]
                segments = [coordinates[i:i + max_coordinates_per_segment] for i in range(0, len(coordinates), max_coordinates_per_segment)]

                # Create a new feature for each segment
                for segment_coords in segments:
                    new_geom = QgsGeometry.fromPolygonXY([segment_coords])
                    new_feature = QgsFeature(fields)
                    new_feature.setGeometry(new_geom)
                    new_feature.setAttributes(feature.attributes())
                    provider.addFeature(new_feature)
        else:
            coordinates = geom.asPolygon()[0]  # Extract the coordinates as a list
            segments = [coordinates[i:i + max_coordinates_per_segment] for i in range(0, len(coordinates), max_coordinates_per_segment)]

            # Create a new feature for each segment
            for segment_coords in segments:
                new_geom = QgsGeometry.fromPolygonXY([segment_coords])
                new_feature = QgsFeature(fields)
                new_feature.setGeometry(new_geom)
                new_feature.setAttributes(feature.attributes())
                provider.addFeature(new_feature)

    # Save the combined layer to a new shapefile
    QgsVectorFileWriter.writeAsVectorFormat(combined_layer, output_file, "utf-8", combined_layer.crs(), "ESRI Shapefile")

    # Unload the layers
    QgsProject.instance().removeMapLayer(layer.id())
    QgsProject.instance().removeMapLayer(combined_layer.id())