import json
import os

import geojson
import numpy as np
import pandas as pd
from shapely.geometry import shape

# set parent folder
parent_folder = '/home/geo/Desktop/codebase/Arches-ETL/data/countries'

# set the output file
outputfile = os.path.join(parent_folder, 'Arches_export.csv')

# set country or group of countries
group_of_countries = True

def list_folders(parent_folder):
    # list the folders in the parent folder
    onlyfolder = [os.path.join(parent_folder, f) for f in os.listdir(parent_folder) if not os.path.isfile(os.path.join(parent_folder, f))]
    return onlyfolder

def list_files(parent_folder, extension = '.json', include = True):
    # list the files in the parent folder
    if include:
        onlyfiles = [os.path.join(parent_folder, f) for f in os.listdir(parent_folder) if os.path.isfile(os.path.join(parent_folder, f)) if f.endswith(extension)]
    else:
        onlyfiles = [os.path.join(parent_folder, f) for f in os.listdir(parent_folder) if os.path.isfile(os.path.join(parent_folder, f)) if not f.endswith(extension)]
    return onlyfiles

if group_of_countries:
    list_of_countries = list_folders(parent_folder)
    print(f'list_of_countries: {[f.split("/")[-1] for f in list_of_countries]}')
else:
    list_of_countries = []
    list_of_countries.append(parent_folder)
    print(f'one country selected; {list_of_countries}')

# read the csv lookup table
df_lookup = pd.read_csv(os.path.join(parent_folder,'Admin resource model lookup.csv'), encoding = 'utf-8', delimiter = ';')

# spilt name value column to a list
df_lookup['Name Value'] = df_lookup['Name Value'].str.split(',', expand=False)

# limit name value column to the first element of the list
df_lookup['Name Value'] = df_lookup['Name Value'].apply(lambda x: x[0])

# set index to polygon name
df_lookup = df_lookup.set_index('Name Value')

print(df_lookup.loc['Botswana']['MAEASaM ID'])


# read the json file
def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# find the polygon id 
def find_polygon_id(json_data):
    if "NAME_1" in json_data["features"][0]['properties']:
        print('Sub-district: ', json_data["features"][0]['properties']["NAME_2"])
        polygon_name = json_data["features"][0]['properties']["NAME_2"]
    elif "ADM1_NAME" in json_data["features"][0]['properties']:
        print('District: ' + json_data["features"][0]['properties']["ADM1_NAME"])
        polygon_name = json_data["features"][0]['properties']["ADM1_NAME"]
    else:
        print("we don't know")
        print(json_data["features"][0]['properties'])
        polygon_name = 'unknown'
    
    # get the polygon ID
    try:
        polygon_id = df_lookup.loc[polygon_name]['MAEASaM ID']
        if type(polygon_id) != str:
            polygon_id = 'conflict'
    except KeyError:
        polygon_id = 'unknown'

    return (polygon_name, polygon_id)

# create output csv file
with open(outputfile, 'w') as f:
    # write header
    f.write('"MAEASaM ID";"name";"geometry"\n')
    # loop through the list of countries
    for country in list_of_countries:
        country_name = country.split('/')[-1]
        print(f'processing {country_name}')
        subfolders = list_folders(country)
        for subfolder in subfolders:
            folder_name = subfolder.split('/')[-1]
            print(f'processing {folder_name}')
            if folder_name == 'Districts':
                districts = list_files(subfolder, extension = '_subdivided.json.geojson', include = True)
                for district in districts:
                    district_name = district.split('/')[-1]
                    print('processing: ' + country_name + ' - ' + district_name)
                    
                    # read the json file
                    json_data = read_json(district)
                    print(district)

                    # find the polygon id
                    polygon_name, polygon_id = find_polygon_id(json_data)
                    
                    # get wkt of the geometry
                    g = geojson.loads(json.dumps(json_data["features"][0]['geometry']))
                    
                    # write the polygon id and wkt to a csv file
                    f.write(f'"{polygon_id}";"{polygon_name}";"{shape(g)}"\n')

            if folder_name == 'sub-districts':
                sub_districts_folders = list_folders(subfolder)
                for sub_districts_folder in sub_districts_folders:
                    district_name = sub_districts_folder.split('/')[-1]
                    print('processing: sub districts of' + country_name + ' - ' + district_name)
                    sub_districts_files = list_files(sub_districts_folder, extension = '_subdivided.json.geojson', include = True)
                    for sub_districts_file in sub_districts_files:
                        sub_districts_name = sub_districts_file.split('/')[-1]
                        print('processing: ' + country_name + ' - ' + district_name + ' - ' + sub_districts_name)
                        
                        # read the json file
                        json_data = read_json(sub_districts_file)
                        print(sub_districts_file)
                        # find the polygon id
                        polygon_name, polygon_id = find_polygon_id(json_data)
                        
                        # get wkt of the geometry
                        g = geojson.loads(json.dumps(json_data["features"][0]['geometry']))
                        
                        # write the polygon id and wkt to a csv file
                        f.write(f'"{polygon_id}";"{polygon_name}";"{shape(g)}"\n')


