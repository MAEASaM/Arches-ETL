import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('all_zim_data_organised.csv')

duplicates = df[df.duplicated(subset=[cMAEASaM ID], keep=False)]

if not duplicates.empty:
    print("Duplicate values in the column:")
    print(duplicates)
else:
    print("There are no duplicate values in the column.")