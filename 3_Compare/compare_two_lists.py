import pandas as pd

# Load the Excel files
modified_EC_class_df = pd.read_excel("/Users/calvincornell/CAZzymes/Book7.xlsx")
EC_ko_df = pd.read_excel("/Users/calvincornell/CAZzymes/Book8_modified.xlsx")

# Define the new column name in the first file
new_column_name = "Kegg_CAZy"

# Initialize an empty list to store the new rows
new_rows = []

# Iterate through each row in the Modified_EC_Class file
for index, row in modified_EC_class_df.iterrows():
    # Get the EC from the current row
    CAZy = row["CAZy"]
    
    # Search for the EC in the EC_Ko file
    maEChing_rows = EC_ko_df[EC_ko_df["CAZy"] == CAZy]
    
    # If a maECh is found
    if not maEChing_rows.empty:
        # Iterate through each maEChing row in the reference file
        for _, maEChing_row in maEChing_rows.iterrows():
            # Get the cell to the right of the maEChing EC
            new_cell_value = maEChing_row.iloc[1]
            
            # Copy the current row from the first file and add the new cell value
            new_row = row.copy()
            new_row[new_column_name] = new_cell_value
            
            # Append the new row to the list of new rows
            new_rows.append(new_row)
    else:
        # If no maECh is found, add an empty value for the new column
        row[new_column_name] = None
        new_rows.append(row)

# Create a DataFrame from the list of new rows
result_df = pd.DataFrame(new_rows)

# Save the modified DataFrame to a new Excel file
result_df.to_excel("/Users/calvincornell/CAZzymes/kegg_CAZymes.xlsx", index=False)

print("The updated file has been saved as 'kegg_CAZymes.xlsx'.")
