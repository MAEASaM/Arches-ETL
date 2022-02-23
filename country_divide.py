# import modules
import os
import processing
from qgis.core import QgsVectorLayer

# set parent folder
parent_folder = ''

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
    country_name = country.split('/')[-1]
    print(f'processing {country_name}')
    subfolders = list_folders(country)
    for subfolder in subfolders:
        folder_name = subfolder.split('/')[-1]
        print(f'processing {folder_name}')
        if folder_name == 'Districts':
            districts = list_files(subfolder, extension = '_subdivided.json.geojson', include = False) 
            for district in districts:
                district_name = district.split('/')[-1]
                print('processing: ' + country_name + ' - ' + district_name)
                district_layer = QgsVectorLayer(district,"distr","ogr")
                processing.run("native:subdivide", {'INPUT': district_layer, "MAX_NODES":MAX_NODES, "OUTPUT":district[:-4]+'_subdivided.json'})
        if folder_name == 'sub-districts':
            sub_districts_folders = list_files(subfolder, extension = '_subdivided.json.geojson', include = False)
            for sub_districts_folder in sub_districts_folders:
                district_name = sub_districts_folder.split('/')[-1]
                print('processing: sub districts of' + country_name + ' - ' + district_name)
                sub_districts_files = list_files(sub_districts_folder)
                for sub_districts_file in sub_districts_files:
                    sub_districts_name = sub_districts_file.split('/')[-1]
                    print('processing: ' + country_name + ' - ' + district_name + ' - ' + sub_districts_name)
                    sub_districts_layer = QgsVectorLayer(sub_districts_file,"sub_distr","ogr")
                    processing.run("native:subdivide", {'INPUT': sub_districts_layer, "MAX_NODES":MAX_NODES, "OUTPUT":sub_districts_file[:-4]+'_subdivided.json'})


'''
Stage Two:
    extract the wkt from the geojson and save it in a csv file
'''
