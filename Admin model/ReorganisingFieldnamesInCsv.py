import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\output_fields.csv')

# Extract the ResourceID column
resource_id_column = df['ResourceID']

# Remove the ResourceID column from the DataFrame
df.drop(columns=['ResourceID'], inplace=True)

# Define the desired order of fieldnames
desired_order = ['ResourceID', 'Name Value', 'Name Type', 'MAEASaM ID', 'Official division', 'Level', 'Discription', 'Created At', 'Comment', 'Country', 'Geometry']

# Insert the ResourceID column at the start
df.insert(0, 'ResourceID', resource_id_column)

# Reorder the DataFrame columns based on the desired order
df = df[desired_order]

# Save the modified DataFrame back to a CSV file
df.to_csv('E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\AdminModel.csv', index=False)
