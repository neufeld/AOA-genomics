import os
import pandas as pd
from collections import defaultdict

# Get the folder name from the user
folder = input("Please enter the folder path: ")

# Dictionary to group files by file name (after the first underscore)
file_groups = defaultdict(list)

# Get a list of all .xlsx files in the folder
files = [f for f in os.listdir(folder) if f.endswith('.xlsx')]

# Group files by file name to the right of the first underscore
for file in files:
    base_name = os.path.splitext(file)[0]
    if '_' in base_name:
        # Split at the first underscore and use everything to the right as the key
        _, key = base_name.split('_', 1)
    else:
        # If there is no underscore in the base_name, use the whole base_name as the key
        key = base_name
    file_groups[key].append(file)

# For each group of files, concatenate columns A and B and remove duplicates from column B
for key, file_list in file_groups.items():
    # Create an empty list to hold dataframes
    dfs = []
    # Read each file in the group
    for file in file_list:
        file_path = os.path.join(folder, file)
        # Read the Excel file with header=None since there are no column headers
        df = pd.read_excel(file_path, header=None, engine='openpyxl')
        # Append the DataFrame (only the first two columns) to the list
        dfs.append(df.iloc[:, :2])
    
    # Concatenate all dataframes vertically
    combined_df = pd.concat(dfs, axis=0)
    
    # Remove duplicates from column B while keeping the first occurrence
    combined_df = combined_df.drop_duplicates(subset=[1], keep='first')
    
    # Add column headers
    combined_df.columns = ['Genes', 'KEGG ID']
    
    # Create an output file name (e.g., "combined_key.xlsx")
    output_filename = f"combined_{key}.xlsx"
    output_filepath = os.path.join(folder, output_filename)
    
    # Save the combined data to a new Excel file with column headers
    combined_df.to_excel(output_filepath, header=True, index=False)
    
    print(f"Combined {len(file_list)} files for key '{key}' and saved to '{output_filepath}'")

print("Finished processing all files.")
