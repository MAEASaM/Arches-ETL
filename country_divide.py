# import modules
import os
import processing
from qgis.core import QgsVectorLayer
from pathlib import Path

# set parent folder
str_path = ""
parent_folder = Path(str_path)
print(parent_folder)

# set country or group of countries
group_of_countries = True

# set max number of nodes
MAX_NODES = 1500

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
    print(list_of_countries)
else:
    list_of_countries = []
    list_of_countries.append(parent_folder)
    print(f'one country selected; {list_of_countries}')

'''
Stage One: 
   divide each polygon into smaller polygons and save them in geojson format 
'''
for country in list_of_countries:
    country_name = country.split('\\')[-1]
    print(f'processing {country_name}')
    subfolders = list_folders(country)
    for subfolder in subfolders:
        level0_folders = list_folders(subfolder)
        folder_name = subfolder.split('\\')[-1]
        print(f'processing folder: {folder_name}')
        if folder_name == 'level0':
            level0 = list_files(subfolder, extension = '_subdivided.json.geojson', include = False) 
            for level0 in level0:
                level0_name = level0.split('\\')[-1]
                print('processing: ' + country_name + ' - ' + level0_name)
                levl0 = QgsVectorLayer(level0,"amd0","ogr")
                processing.run("native:subdivide", {'INPUT': level0, "MAX_NODES":MAX_NODES, "OUTPUT":level0[:-4]+'_subdivided.json'})
    for subfolder in subfolders:
        level1_folders = list_folders(subfolder)
        folder_name = subfolder.split('\\')[-1]
        print(f'processing folder: {folder_name}')
        if folder_name == 'level1':
            level1 = list_files(subfolder, extension = '_subdivided.json.geojson', include = False) 
            for level1 in level1:
                level1_name = level1.split('\\')[-1]
                print('processing: ' + country_name + ' - ' + level0_name + '-' + level1_name)
                levl1 = QgsVectorLayer(level1,"amd0","ogr")
                processing.run("native:subdivide", {'INPUT': level1, "MAX_NODES":MAX_NODES, "OUTPUT":level1[:-4]+'_subdivided.json'})
    for subfolder in subfolders:
        level2_folders = list_folders(subfolder)
        folder_name = subfolder.split('\\')[-1]
        print(f'processing folder: {folder_name}')
        if folder_name == 'level2':
            level2 = list_files(subfolder, extension = '_subdivided.json.geojson', include = False) 
            for level2 in level2:
                level2_name = level2.split('\\')[-1]
                print('processing: ' + country_name + ' - ' + level0_name + '-' + level1_name + '-' + level2_name)
                levl2 = QgsVectorLayer(level2,"amd0","ogr")
                processing.run("native:subdivide", {'INPUT': level2, "MAX_NODES":MAX_NODES, "OUTPUT":level2[:-4]+'_subdivided.json'})          


'''
Stage Two:
    extract the wkt from the geojson and save it in a csv file
'''
