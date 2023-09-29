### This script is used to clean the CSV files for the Arches upload
### The script is written by Renier Van Der Merwe and Mahmoud Abdelrazek

### TODO:
# 1. Refactor actor_uuid_format function to generate the actor dict only once # Done
# 2. Add check for the geomtry and fix duplicate point problem
# 3. split the filtering function to aliases and data fixes
# 4. generalise the script to work with other csv files



# Data sheets
input_csv_file = "E:\MAEASaM\MAEASaM_desktop\Arches\Arches upload files\Remote sensing\Sudan_BulkUploadTrial.csv"
output_csv_file = "E:\MAEASaM\MAEASaM_desktop\Arches\Arches upload files\Remote sensing\SudanBulkUploadEdElias2023_newGeoRH.csv"
actor_csv_file = "E:\MAEASaM\MAEASaM_desktop\Arches\Arches upload files\Remote sensing\Actor.csv"


import csv
from datetime import datetime

def read_input_csv() -> csv.DictReader:
    with open(input_csv_file, 'r') as input_csv_file_object:
        input_csv_file_object_reader = csv.DictReader(input_csv_file_object)

        return input_csv_file_object_reader

def read_actor_uuid_csv() -> dict:
    actor_uuid_dict = {}
    with open(actor_csv_file, 'r') as actor_uuid_file_object:
        actor_uuid_file_object_reader = csv.DictReader(actor_uuid_file_object)
        for uuid_row in actor_uuid_file_object_reader:
            actor_uuid_dict[uuid_row["Name value"]] = uuid_row["resourceid"]

    return actor_uuid_dict


def check_for_resource_id_column(file_reader: csv.DictReader) -> bool:
    return "ResourceID" in file_reader.fieldnames     

def write_output_csv(file_reader: csv.DictReader) -> None:
    with open(output_csv_file,'w') as sudan_geometry_overwritten:
        
        # read actor uuid csv
        actor_uuid_dict = read_actor_uuid_csv()

        fieldnames = file_reader.fieldnames
        missing_resource_id = check_for_resource_id_column(file_reader)
        
        if not missing_resource_id:
            fieldnames = ["ResourceID"] + fieldnames
    
        writer = csv.DictWriter(sudan_geometry_overwritten, fieldnames=fieldnames)

        writer.writeheader()
        for row in file_reader:
            if not missing_resource_id:
                row["ResourceID"] = row["MAEASaM ID"]

            row = data_filter(row)
            row = date_format_all_coloums(row)
            row = actor_uuid_format(row, actor_uuid_dict)
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
    if row["Image Type"] == "CNES / Airbus":
        row["Image Type"] = "CNES Airbus"
    if row["Image Type"] == "Bung":
        row["Image Type"] = "Bing"
    if row["Climate Zone"] == "Dry Winter-Hot Summer (t)":
        row["Climate Zone"] = "Temperate Dry Winter Hot summer"
    if row["Climate Zone"] == "Dry Winter-Warm Summer (t)":
        row["Climate Zone"] = "Temperate Dry Winter Warm summer"
    if row["Surveyor Name"] == "Ed Burnett":
        row["Surveyor Name"] = "Ed Burnett, Edward Burnett"
    if row["Threat assessor name"] == "Ed Burnett":
        row["Threat assessor name"] = "Ed Burnett, Edward Burnett"
    if row["Measurement unit"] == "m2":
        row["Measurement unit"] = "square meter"
    if row["Measurement unit"] == "m":
        row["Measurement unit"] = "Meter"
    if row["Measurement unit"] == "Hectares":
        row["Measurement unit"] = "Hectare"
    if row["Additional information"] == "M":
        row["Additional information"] = ""
    if row["Survey type"] == "Historic maps check":
        row["Survey type"] = "Historic map check"
    if row["Threat type"] == "Conflict":
        row["Threat type"] = "War"
    if row["Threat type"] == "Occupation expansion":
        row["Threat type"] = "Urbanisation"
    if row["Evidence Shape"] == "Ring":
        row["Evidence Shape"] = "Circular"
    if row["Ground truthed"] == "#REF!":
        row["Ground truthed"] = "No"
    if row["Land use land cover"] == "Built-up":
        row["Land use land cover"] = "Built up"
    return row

def convert_date_format(date_str: str) -> str:
    try:
        # Parse the input date in the current format
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        # Convert it to the desired format "%Y-%m-%d"
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        # Handle invalid date format gracefully
        return date_str  # Return the original date if it can't be parsed

def date_format_all_coloums(row: dict) -> dict:
    row["Survey Date"] = convert_date_format(row["Survey Date"])
    row["Date of imagery"] = convert_date_format(row["Date of imagery"])
    row["Date of imagery"] = row["Date of imagery"].replace("20XX", row["Survey Date"])
    row["Date of imagery"] = row["Date of imagery"].replace("1900-01-00", row["Survey Date"])
    row["Threat assessment date"] = convert_date_format(row["Threat assessment date"])
    row["Image used date"] = convert_date_format(row["Image used date"])
    return row


def actor_uuid_format(row: dict, actor_uuid_dict) -> dict:
    row["Surveyor Name"] = "[{'resourceId': '"+ actor_uuid_dict[row["Surveyor Name"]] + "','ontologyProperty': 'http://www.cidoc-crm.org/cidoc-crm/P11_had_participant', 'resourceXresourceId': '','inverseOntologyProperty': 'http://www.cidoc-crm.org/cidoc-crm/P140_assigned_attribute_to'}]"
    row["Threat assessor name"] = "[{'resourceId': '"+ actor_uuid_dict[row["Threat assessor name"]] + "','ontologyProperty': 'http://www.cidoc-crm.org/cidoc-crm/P11_had_participant', 'resourceXresourceId': '','inverseOntologyProperty': 'http://www.cidoc-crm.org/cidoc-crm/P140_assigned_attribute_to'}]"

    return row

def clean_geomtry_based_on_type(row: dict) -> dict:
    geometry = row["Geometry"]
    if geometry:
        geometry_type = geometry.split(" ")[0]
        if geometry_type == "POINT":
            return row
        elif geometry_type == "MULTIPOLYGON":
            row["Geometry"] = remove_duplicate_points_from_multipolygon(geometry)
            return row
        else:
            print("Unknown geometry type: " + geometry_type)
        

def remove_duplicate_points_from_multipolygon(geometry: str) -> str:
    return geometry

if __name__ == '__main__':
    write_output_csv(read_input_csv())
