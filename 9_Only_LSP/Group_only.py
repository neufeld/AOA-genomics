import pandas as pd
import os

# Prompt the user to enter the full path to the input .xlsx file
input_file_path = input("Please enter the full path to the input .xlsx file: ")

# Load the Excel file into a DataFrame
df = pd.read_excel(input_file_path)

# Prompt the user to specify the column to use for unique groups
group_column = input("Please specify the column to use for unique groups: ")

# Check if the specified column exists in the DataFrame
if group_column not in df.columns:
    print(f"Error: The specified column '{group_column}' does not exist in the input file.")
else:
    # Get the unique groups from the specified column
    unique_groups = df[group_column].unique()

    # Define the input file directory
    input_file_directory = os.path.dirname(input_file_path)
    
    # Extract the base name of the input file (minus the extension)
    input_file_base_name = os.path.splitext(os.path.basename(input_file_path))[0]
    
    # Create a new directory for the output files
    output_folder_path = os.path.join(input_file_directory, input_file_base_name)
    os.makedirs(output_folder_path, exist_ok=True)
    
    # Iterate through each unique group
    for group in unique_groups:
        # Filter the DataFrame for the current group
        group_df = df[df[group_column] == group]
        
        # Dictionary to store the exclusive columns for the current group
        exclusive_columns = {}
        
        # Iterate through each column in the DataFrame (excluding the grouping column)
        for column in df.columns:
            if column != group_column:
                # Check if the column contains any instance of 1 for the current group
                group_contains_one = group_df[column].any()
                
                # Check if the column contains no instance of 1 for other groups
                other_groups_absent = (df[df[group_column] != group][column] == 0).all()
                
                # If both conditions are met, the column is exclusive to the current group
                if group_contains_one and other_groups_absent:
                    exclusive_columns[column] = group_df[column]
        
        # If there are exclusive columns for the group, save them to a new .xlsx file
        if exclusive_columns:
            # Create a new DataFrame from the exclusive columns dictionary
            exclusive_df = pd.DataFrame(exclusive_columns)
            
            # Insert the grouping column as the first column in the DataFrame
            exclusive_df.insert(0, group_column, group_df[group_column].values)
            
            # If the "Species" column exists, insert it as the next column in the DataFrame
            if "Species" in group_df.columns:
                exclusive_df.insert(1, "Species", group_df["Species"].values)
            
            # Define the output file path using the output folder path and the group name
            output_file_path = os.path.join(output_folder_path, f"{group}_exclusive_columns.xlsx")
            
            # Save the DataFrame to an Excel file
            exclusive_df.to_excel(output_file_path, index=False)
            
            print(f"Saved exclusive columns for group '{group}' to {output_file_path}")
