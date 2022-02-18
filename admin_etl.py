# transform Arches exported admin file to Arches input format

# import modules
import csv
import uuid
from dateutil import parser
from geomet import wkt
from itertools import tee

# read the input csv as a list of dicts
reader = csv.DictReader(open('data/Admin resource model.xlsx.csv'), delimiter=';')

def split_row_to_cards(attr):
    #split row into cards   
    split_attr = attr.split(',')
    attr_list = []
    combine_string = ''
    for j in split_attr:
        # first case (first value in list)
        if combine_string == '':
            combine_string += j.strip()

        # second case (a new card)
        elif j[0] == ' ':
            attr_list.append(combine_string)
            combine_string = ''
            combine_string += j.strip()

        # third case (same card)
        elif j[0] != ' ':
            combine_string = combine_string + ', ' + j.strip()
    
    if combine_string != '':
        attr_list.append(combine_string)

    return(attr_list)

def match_length(attr_list, attr_type_list):
    # match the length of the list of cards to the list of attribute types
    #print(f'before matching {attr_list}, {attr_type_list}')
    if len(attr_list) > len(attr_type_list):
        for i in range(len(attr_list) - len(attr_type_list)):
            attr_type_list.append(attr_type_list[-1])
    elif len(attr_list) < len(attr_type_list):
        #print(f'length of name list: {attr_list}')
        attr_type_list[0] = ','.join(attr_type_list)
        attr_type_list = attr_type_list[0:1]
    #print(f'inside the function: {attr_list}, {attr_type_list}')
    return(attr_list, attr_type_list)

# list incompelte geometry
faulty_geom_id = []

# set counters for faulty and complete geometries
faulty_geom_counter = 0
complete_geom_counter = 0

# write the output file in Arches input format
with open('data/Admin resource model modifed.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_ALL)
    writer.writerow(['ResourceID','Name Type','Resource created at','Resource last modified at','MAEASaM ID','Comment','Name Value','Geometry','Description','Level'])

    # copy itterator 
    reader_iter, counter_iter = tee(reader)

    # count the number of rows
    row_count = sum(1 for row in counter_iter)

    # set row counter
    row_counter = 0

    # loop through the input csv
    for row in reader_iter:

        # increment row counter
        row_counter += 1

        # print progress
        print(f'processing row {row_counter} out of {row_count}')
        
        # check if geometry is valid
        try:
            geo_checker = wkt.loads(row['Geometry'])
            complete_geom_counter += 1
        except:
            faulty_geom_id.append(row['MAEASaM ID'])
            faulty_geom_counter += 1
            continue

        # get the id of the row
        ID=str(uuid.uuid4())
        
        # split the name values and types and count them
        name_list = [name.strip() for name in row['Name Value'].split(',') if '?' not in name]
        name_type_list = split_row_to_cards(row['Name Type'])
        if len(name_list) != len(name_type_list):
            name_list, name_type_list = match_length(name_list, name_type_list)
        #print(f'outside the list {name_list}, {name_type_list}')
        no_rows_per_resource = max([len(name_list), len(name_type_list)])
        
        # fix date format
        date_created = parser.parse(row['Resource created at']).strftime('%Y-%m-%d')
        date_modified = parser.parse(row['Resource last modified at ']).strftime('%Y-%m-%d')

        # write the first row of the resource
        writer.writerow([ID,name_type_list[0],date_created,date_modified,row['MAEASaM ID'],row['Comment'],name_list[0],row['Geometry'],row['Description'],row['Level']])

        # write the rest of the rows
        if no_rows_per_resource > 1:
            for i in range(1,no_rows_per_resource):
                writer.writerow([ID,name_type_list[i],'','','','',name_list[i],'','',''])

# write the list of faulty geometry ids
with open('data/faulty_geom_id.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_ALL)
    writer.writerow(['MAEASaM ID'])
    for i in faulty_geom_id:
        writer.writerow([i])

# print final results
print(f'processing compelete! \ntotal row count: {row_count}\nfaulty geometries: {faulty_geom_counter}\ncomplete geometries: {complete_geom_counter}')
