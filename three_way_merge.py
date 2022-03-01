'''This is a small script to merge the three files with Administrative divisions data into one file.'''

# Importing the libraries
import pandas as pd

# Importing the three files
df_main = pd.read_csv('/home/geo/Desktop/codebase/Arches-ETL/data/new_list/new_order.csv', delimiter=';') # Main file that has the correct order of Admin divisions
df_geom = pd.read_csv('/home/geo/Desktop/codebase/Arches-ETL/data/new_list/geom.csv', delimiter=';') # File with the geometries of the Admin divisions
df_attr_renier = pd.read_csv('/home/geo/Desktop/codebase/Arches-ETL/data/new_list/attr_renier.csv', delimiter=';') # File with the attributes of the Admin divisions recorded by Renier
df_attr_serge = pd.read_csv('/home/geo/Desktop/codebase/Arches-ETL/data/new_list/attr_serge.csv', delimiter=';') # File with the attributes of the Admin divisions recorded by Serge

# concat attributes files
df_attr = pd.concat([df_attr_renier, df_attr_serge], axis=0, ignore_index=True)

# clean the files and extract a common column
# clean the attributes file
df_attr['name_match'] = df_attr['Name Value'].str.split(',').str[0]
df_attr['name_match'] = df_attr['name_match'].str.strip().str.lower()
df_attr = df_attr[['Name Type', 'Resource created at', 'Resource last modified at ',
       'Comment', 'Name Value', 'Description',
       'Level', 'name_match']]

# cell the geometries file
df_geom = df_geom[['name', 'geometry']]
df_geom['name'] = df_geom['name'].str.strip().str.lower()

# clean the main file
df_main['name'] = df_main['name'].str.strip().str.lower()

# # merge the files
df_merged = pd.merge(df_main, df_attr, left_on='name', right_on='name_match', how='left')
df_merged = pd.merge(df_merged, df_geom, left_on='name', right_on='name', how='left')

df_merged.to_csv('/home/geo/Desktop/codebase/Arches-ETL/data/new_list/new_order_merged.csv', sep=';', index=False)
