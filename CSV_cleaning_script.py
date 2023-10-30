# This script is used to clean the CSV files for the Arches upload
# The script is written by Mahmoud Abdelrazek and Renier van der Merwe

# TODO:
# 1. Refactor actor_uuid_format function to generate the actor dict only once # Done
# 2. Add check for the geomtry and fix duplicate point problem
# 3. split the filtering function to aliases and data fixes
# 4. generalise the script to work with other csv files
# 5. Allow for multiple date formates to be corrected to the require formate
# 6. Add section that orgnises the MAEASaM ID numericaly from the input csv


# Data sheets

input_csv_file = "Sudan_BulkUploadTrial (1).csv"
output_csv_file = "zim_modified.csv"
actor_csv_file = "Actor.csv"


import pandas as pd
import csv
from datetime import datetime
import pathlib
from shapely import wkt
from shapely.geometry import MultiPolygon, Polygon, Point


# find the path of the script
script_path = pathlib.Path(__file__).parent.absolute()

# add script path to the csv files
input_csv_file = script_path / input_csv_file
output_csv_file = script_path / output_csv_file
actor_csv_file = script_path / actor_csv_file


class csv_cleaner:
    def __init__(self, main_input_file):
        self.main_input_df = pd.read_csv(main_input_file)
        self.working_drictory = pathlib.Path(main_input_file).parent.absolute()
        self.output_csv_name_and_directory = self.working_drictory / (
            pathlib.Path(main_input_file).stem + "_cleaned.csv"
        )

    def read_name_uuid_supportive_file(self, file_name: str or pathlib.Path) -> dict:
        name_uuid_supportive_file = pd.read_csv(file_name)
        name_uuid_supportive_dict = pd.Series(
            name_uuid_supportive_file["Name value"].values,
            index=name_uuid_supportive_file["resourceid"],
        ).to_dict()
        return name_uuid_supportive_dict

    def read_replacment_supportive_file(self, file_name: str or pathlib.Path) -> dict:
        name_uuid_supportive_file = pd.read_csv(file_name)
        return name_uuid_supportive_file

    def check_for_resource_id_column(self) -> bool:
        return "ResourceID" in self.main_input_df.keys()

    def add_resource_id_column(self) -> None:
        if not self.check_for_resource_id_column():
            self.main_input_df["ResourceID"] = self.main_input_df["MAEASaM ID"]

    def add_resource_instace_json(
        self,
        value_uuid_dict: dict,
        col_name: str,
        forward_property: str = "http://www.cidoc-crm.org/cidoc-crm/P11_had_participant",
        inverse_property: str = "http://www.cidoc-crm.org/cidoc-crm/P140_assigned_attribute_to",
    ) -> None:
        self.main_input_df[col_name] = self.main_input_df[col_name].apply(
            lambda x: (
                "[{'resourceId': '"
                + value_uuid_dict[x]
                + "','ontologyProperty': '"
                + forward_property
                + "', 'resourceXresourceId': '','inverseOntologyProperty': '"
                + inverse_property
                + "'}]"
            )
            if x in value_uuid_dict.keys()
            else ""
        )

    def covert_date_format(self, date_str: str) -> str:
        try:
            date_obj = datetime.strptime(
                date_str, "%d/%m/%Y", "%Y/%m/%d", "%Y-%m-%d", "%m/%d/%Y", "%d-%m"
            )
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            return date_str

    def date_format_list_of_coloums(self, row: dict, date_cloumn_names: list) -> None:
        for date_cloumn_name in date_cloumn_names:
            self.main_input_df[date_cloumn_name] = self.main_input_df[
                date_cloumn_name
            ].apply(self.covert_date_format)

    def replace_value_in_coloum(
        self, coloum_name: str, old_value: str, new_value: str
    ) -> None:
        self.main_input_df[coloum_name] = self.main_input_df[coloum_name].replace(
            old_value, new_value
        )

    def stream_replace_value_in_coloum(self, replacement_df: pd.DataFrame) -> None:
        for index, row in replacement_df.iterrows():
            self.replace_value_in_coloum(
                row["coloum_name"], row["old_value"], row["new_value"]
            )

    def copy_value_from_coloum_to_coloum_on_optioanl_condation(
        self, source_coloum_name: str, target_coloum_name: str, condation_value: str
    ) -> None:
        self.main_input_df[target_coloum_name] = self.main_input_df.apply(
            lambda x: x[target_coloum_name]
            if x[condation_value]
            else x[source_coloum_name],
            axis=1,
        )

    def stream_copy_value_from_coloum_to_coloum(
        self, replacement_df: pd.DataFrame
    ) -> None:
        for index, row in replacement_df.iterrows():
            self.copy_value_from_coloum_to_coloum_on_optioanl_condation(
                row["source_coloum_name"],
                row["target_coloum_name"],
                row["condation_value"],
            )

    def remove_duplicate_points(self, geometry_wkt: str) -> str:
        if not geometry_wkt:
            return ""

        if type(geometry_wkt) == str:
            geometry = wkt.loads(geometry_wkt)
        else:
            geometry = geometry_wkt

        seen_points = set()

        if isinstance(geometry, MultiPolygon):
            new_polygons = []
            for polygon in geometry.geoms:
                new_polygon = self.remove_duplicate_points(polygon)
                new_polygons.append(new_polygon)
            return MultiPolygon(new_polygons)
        elif isinstance(geometry, Polygon):
            new_exterior = []
            for point in geometry.exterior.coords:
                if point not in seen_points:
                    seen_points.add(point)
                    new_exterior.append(point)
            new_interiors = []
            for interior in geometry.interiors:
                new_interior = []
                for point in interior.coords:
                    if point not in seen_points:
                        seen_points.add(point)
                        new_interior.append(point)
                new_interiors.append(new_interior)

            return Polygon(shell=new_exterior, holes=new_interiors)
        else:
            return geometry

    def clean_geomtry_based_on_type(
        self, geometry_column_name: str = "geometry"
    ) -> dict:
        # currently cleans only the multipolygon geometry. Needs more to be gneneralized for other types
        self.main_input_df[geometry_column_name] = self.main_input_df[
            geometry_column_name
        ].apply(
            lambda x: (
                self.remove_duplicate_points(x)
                if x.split(" ")[0] == "MULTIPOLYGON"
                else x
            )
        )

    def write_output_csv(self) -> None:
        self.main_input_df.to_csv(self.output_csv_name_and_directory, index=False)

    def clean_file(
        self,
        name_uuid_supportive_file=None,
        resource_instace_column_list=[],
        replacment_supportive_file=None,
        date_format_coloums=[],
    ) -> None:
        if name_uuid_supportive_file and len(resource_instace_column_list) > 0:
            name_uuid_supportive_dict = self.read_name_uuid_supportive_file(
                name_uuid_supportive_file
            )
            for resource_instace_column in resource_instace_column_list:
                self.add_resource_instace_json(
                    name_uuid_supportive_dict, resource_instace_column
                )
        if replacment_supportive_file:
            replacment_supportive_df = self.read_replacment_supportive_file(
                replacment_supportive_file
            )
            if all(
                x in replacment_supportive_file.keys
                for x in ["condation_value", "target_coloum_name", "source_coloum_name"]
            ):
                self.stream_copy_value_from_coloum(replacment_supportive_df)
            elif all(
                x in replacment_supportive_file.keys
                for x in ["old_value", "new_value", "coloum_name"]
            ):
                self.stream_replace_value_in_coloum(replacment_supportive_df)
            else:
                pass
        if len(date_format_coloums) > 0:
            self.date_format_list_of_coloums(date_format_coloums)
        self.clean_geomtry_based_on_type()
        self.write_output_csv()


def date_format_all_coloums(row: dict) -> dict:
    row["Date of imagery"] = row["Date of imagery"].replace("20XX", row["Survey date"])
    row["Date of imagery"] = row["Date of imagery"].replace(
        "1900-01-00", row["Survey date"]
    )

    return row


def write_output_csv(file_reader: csv.DictReader) -> None:
    with open(output_csv_file, "w") as zim_data_overwritten:
        # read actor uuid csv
        actor_uuid_dict = read_actor_uuid_csv()

        fieldnames = file_reader.fieldnames
        missing_resource_id = check_for_resource_id_column(file_reader)

        if not missing_resource_id:
            fieldnames = ["ResourceID"] + fieldnames

        writer = csv.DictWriter(zim_data_overwritten, fieldnames=fieldnames)

        writer.writeheader()
        for row in file_reader:
            if not missing_resource_id:
                row["Geometry type"] = row[
                    "WKT"
                ]  # This is just a fix for my csv. We will have to change it to do this only if a WKT coloum is pressent

            row = data_filter(row)
            row = date_format_all_coloums(row)
            row = actor_uuid_format(row, actor_uuid_dict)
            row = clean_geomtry_based_on_type(row)
            writer.writerow(row)


def data_filter(row: dict) -> dict:
    if row["Evidence"] == "Building":
        row["Evidence"] = "Structure"
    if row["Evidence"] == "Structures":
        row["Evidence"] = "Structure"
    if row["Evidence"] == "Unknown":
        row["Evidence"] = "Standing remains"
    if row["Evidence"] == "Enclosures":
        row["Evidence"] = "Enclosure"
    if row["Evidence"] == "Terracing":
        row["Evidence"] = "Terrace"
    if row["Evidence"] == "Wall":
        row["Evidence"] = "Walling"
    if row["Evidence"] == "Stone Mound":
        row["Evidence"] = "Stone mound"
    if row["Evidence"] == "Soil Mark":
        row["Evidence"] = "Soil mark"
    if row["Evidence"] == "Complex Enclosure":
        row["Evidence"] = "Complex enclosure"
    if row["Evidence"] == "Complex enclosures":
        row["Evidence"] = "Complex enclosure"
    if row["Evidence"] == "Stone Circle":
        row["Evidence"] = "Stone circle"
    if row["Evidence"] == "Complex Structure":
        row["Evidence"] = "Complex structure"
    if row["Evidence"] == "Earth":
        row["Evidence"] = "Terrace"
    if row["Evidence"] == "Soil discoloration":
        row["Evidence"] = "Discolouration"
    if row["Image type"] == "CNES / Airbus":
        row["Image type"] = "CNES Airbus"
    if row["Image type"] == "CNES/Airbus":
        row["Image type"] = "CNES Airbus"
    if row["Image type"] == "Bung":
        row["Image type"] = "Bing"
    if row["Climatic zone"] == "Dry Winter-Hot Summer (t)":
        row["Climatic zone"] = "Temperate Dry Winter Hot summer"
    if row["Climatic zone"] == "Dry Winter-Warm Summer (t)":
        row["Climatic zone"] = "Temperate Dry Winter Warm summer"
    if row["Climatic zone"] == "Cwb":
        row["Climatic zone"] = "Temperate Dry Winter Warm summer"
    if row["Climatic zone"] == "Cwa":
        row["Climatic zone"] = "Temperate Dry Winter Hot summer"
    if row["Climatic zone"] == "Bsh":
        row["Climatic zone"] = "Steppe Hot"
    if row["Surveyor name"] == "Ed Burnett":
        row["Surveyor name"] = "Ed Burnett, Edward Burnett"
    if row["Surveyor name"] == "Renier van der Merwe":
        row["Surveyor name"] = "Renier Hendrik van der Merwe"
    if row["Threat assessor name"] == "Ed Burnett":
        row["Threat assessor name"] = "Ed Burnett, Edward Burnett"
    if row["Threat assessor name"] == "Renier van der Merwe":
        row["Threat assessor name"] = "Renier Hendrik van der Merwe"
    if row["Measurement unit"] == "m2":
        row["Measurement unit"] = "square meter"
    if row["Measurement unit"] == "Square Meter":
        row["Measurement unit"] = "square meter"
    if row["Measurement unit"] == "m":
        row["Measurement unit"] = "Meter"
    if row["Measurement unit"] == "meter":
        row["Measurement unit"] = "Meter"
    if row["Measurement unit"] == "Hectares":
        row["Measurement unit"] = "Hectare"
    if row["Measurement type"] == "Perimiter":
        row["Measurement type"] = "Area"
    if row["Additional information"] == "M":
        row["Additional information"] = ""
    if row["Survey type"] == "Historic maps check":
        row["Survey type"] = "Historic map check"
    if row["Survey type"] == "Topographic":
        row["Survey type"] = "Topographic other"
    if row["Threat type"] == "Conflict":
        row["Threat type"] = "War"
    if row["Threat type"] == "Occupation expansion":
        row["Threat type"] = "Urbanisation"
    if row["Threat type"] == "Environmental":
        row["Threat type"] = "Episodic events"
    if row["Threat type"] == "Environmental ":
        row["Threat type"] = "Episodic events"
    if row["Threat type"] == "Anthopogenic":
        row["Threat type"] = "Agriculture"
    if row["Threat type"] == "Anthropogenic":
        row["Threat type"] = "Agriculture"
    if row["Threat type"] == "Antrhopgenic":
        row["Threat type"] = "Agriculture"
    if row["Threat type"] == "Antrhopogenic":
        row["Threat type"] = "Agriculture"
    if row["Threat type"] == "Development":
        row["Threat type"] = "Urbanisation"
    if row["Evidence shape"] == "Ring":
        row["Evidence shape"] = "Circular"
    if row["Ground truthed"] == "#REF!":
        row["Ground truthed"] = "No"
    if row["Land use land cover"] == "Built-up":
        row["Land use land cover"] = "Built up"
    if row["Land use land cover"] == "grassland":
        row["Land use land cover"] = "Grassland"
    if row["Land use land cover"] == "Cropland":
        row["Land use land cover"] = "Cultivated"
    if row["Land use land cover"] == "Tree Cover":
        row["Land use land cover"] = "Thicket"
    if row["Land use land cover"] == "Shurbland":
        row["Land use land cover"] = "Scrub"
    if row["Land use land cover"] == "Bare rock or Soil discoloration":
        row["Land use land cover"] = "Bare rock or soil"
    if row["Land use land cover"] == "Bare":
        row["Land use land cover"] = "Bare rock or soil"
    return row


if __name__ == "__main__":
    # read_input_csv()
    csv_file_cleaner_instance = csv_cleaner(input_csv_file)
    csv_file_cleaner_instance.add_resource_id_column
    csv_file_cleaner_instance.write_output_csv()
