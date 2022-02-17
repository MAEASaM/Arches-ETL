# transform Arches exported admin file to Arches input format

# import modules
import csv
import uuid
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
    print(f'before matching {attr_list}, {attr_type_list}')
    if len(attr_list) > len(attr_type_list):
        for i in range(len(attr_list) - len(attr_type_list)):
            attr_type_list.append(attr_type_list[-1])
    elif len(attr_list) < len(attr_type_list):
        print(f'length of name list: {attr_list}')
        attr_type_list[0] = ','.join(attr_type_list)
        attr_type_list = attr_type_list[0:1]
    print(f'inside the function: {attr_list}, {attr_type_list}')
    return(attr_list, attr_type_list)

# write the output file in Arches input format
with open('data/Admin resource model modifed.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['Name Type','Resource created at','Resource last modified at','MAEASaM ID','Comment','Name Value','Geometry','Description','Level'])
    for row in reader:
        # get the id of the row
        ID=row['MAEASaM ID'].strip()
        # split the name values and types and count them
        name_list = [name.strip() for name in row['Name Value'].split(',') if '?' not in name]
        name_type_list = split_row_to_cards(row['Name Type'])
        if len(name_list) != len(name_type_list):
            name_list, name_type_list = match_length(name_list, name_type_list)
        print(f'outside the list {name_list}, {name_type_list}')
        no_rows_per_resource = max([len(name_list), len(name_type_list)])
        # write the row for each name value
        writer.writerow([name_type_list[0],row['Resource created at'],row['Resource last modified at '],ID,row['Comment'],name_list[0],row['Geometry'],row['Description'],row['Level']])

        # write the rest of the rows
        if no_rows_per_resource > 1:
            for i in range(1,no_rows_per_resource):
                writer.writerow([name_type_list[i],'','',ID,'',name_list[i],'','',''])
        
