import pandas as pd

# Path to the first Excel file
file1_path = '/Users/calvincornell/BB/output_processed_2.xlsx'

# Path to the second Excel file
file2_path = '/Users/calvincornell/BB/query_lists.xlsx'

# Read both Excel files
df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)

# Extract the "Kegg" column from the first file
kegg_column = df1['Kegg']

# Initialize a dictionary to store the presence (1) or absence (0) for each entry
presence_dict = {}

# Iterate over columns of the second file to maintain the order
for column in df2.columns:
    # Check if the column is the "Kegg" column of the first file
    if column == 'Kegg':
        continue  # Skip comparison with the same column
        
    # Determine presence (1) or absence (0) for each entry in the "Kegg" column
    presence_dict[column] = [1 if entry in df2[column].values else 0 for entry in kegg_column]

# Create a DataFrame from the presence dictionary, using the column order from the query file
result_df = pd.DataFrame(presence_dict, columns=df2.columns)

# Copy the first two columns from the first file to the new DataFrame
result_df.insert(0, 'Kegg', df1['Kegg'])
result_df.insert(1, 'Rxns', df1['Rxns'])

# Save the result as a new Excel file
result_df.to_excel('/Users/calvincornell/BB/output.xlsx', index=False)
