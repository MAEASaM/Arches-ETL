import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('all_zim_data_organised.csv')

# Define a function to generate unique identifiers
def generate_identifier(index):
    base = "RS-ZWE-"
    num_zeros = max(7 - len(str(index)), 0)
    return f"{base}{'0'*num_zeros}{index}"

# Create a new column with the generated identifiers
df['MAEASaM ID'] = df.index + 1  # Start from 1
df['MAEASaM ID'] = df['MAEASaM ID'].map(generate_identifier)

# Save the DataFrame back to a CSV file if needed
df.to_csv('output_file.csv', index=False)

# Display the DataFrame with the new identifiers
print(df)