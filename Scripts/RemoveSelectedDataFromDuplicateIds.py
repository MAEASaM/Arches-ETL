import pandas as pd

# Load the CSV file into a pandas DataFrame(df)
df = pd.read_csv(
    "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\Admin model\\AdminModelSimplifiedSubdivided.csv"
)

# Specify the header you want to examine for duplicates
header_to_check = "MAEASaM ID"

# Create a set to keep track of duplicated IDs
seen_ids = set()

# Iterate through the DataFrame
for index, row in df.iterrows():
    current_id = row[header_to_check]

    # Check if the ID is duplicated
    if current_id in seen_ids:
        # Remove data from specific headers for subsequent occurrences
        df.at[index, "MAEASaM ID"] = None  # Header to remove
        df.at[index, "Name value"] = None  # Header to remove
        df.at[index, "Name type"] = None  # Header to remove
        df.at[index, "Official division"] = None  # Header to remove
        df.at[index, "Administration level"] = None  # Header to remove
        df.at[index, "Description"] = None  # Header to remove
        df.at[index, "Resource created at"] = None  # Header to remove
        df.at[index, "Comment"] = None  # Header to remove
        df.at[index, "Country"] = None  # Header to remove

    else:
        # If the ID is not duplicated, add it to the set
        seen_ids.add(current_id)

# Sort the DataFrame based on 'ResourceID'
df.sort_values(by="ResourceID", inplace=True)

# Save the modified DataFrame back to a CSV file
output_path = "E:\\MAEASaM\\MAEASaM_desktop\\Arches\\Arches Git\\Arches-ETL\\Admin model\\AdminModelSimplifiedSubdividedOrdered.csv"
df.to_csv(output_path, index=False)
