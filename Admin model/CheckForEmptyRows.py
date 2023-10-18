import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
csv_file = 'E:\MAEASaM\MAEASaM_desktop\Arches\Arches Git\Arches-ETL\Admin model\AdminModel.csv'

# Replace 'MAEASaM ID' with the actual name of the column you want to check
column_name = 'MAEASaM ID'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Check for empty values in the specified column
empty_rows = df[df[column_name].isnull()]

# Print the rows with empty values in the specified column
print(empty_rows)