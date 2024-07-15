import pandas as pd

# Load the Excel file
file_path = "/Users/calvincornell/BB/output_combined.xlsx"
df = pd.read_excel(file_path)

# Select columns C to BH
selected_columns = df.iloc[:, 2:61]

# Remove commas and empty spaces, convert entries to numbers
selected_columns = selected_columns.replace({'[, ]': ''}, regex=True).apply(pd.to_numeric, errors='coerce')

# Set values greater than 1 to 1 and values equal to or less than 0 to 0
selected_columns = selected_columns.applymap(lambda x: 1 if x > 0 else 0)

# Copy the first two columns from the original DataFrame
first_two_columns = df.iloc[:, :2]

# Ensure the first two columns have the same length as selected_columns
num_rows_selected = selected_columns.shape[0]
first_two_columns = first_two_columns.iloc[:num_rows_selected, :]

# Concatenate the first two columns with the modified DataFrame
modified_df = pd.concat([first_two_columns, selected_columns], axis=1)

# Save the modified DataFrame to a new Excel file
output_file_path = "/Users/calvincornell/BB/output_modified.xlsx"
modified_df.to_excel(output_file_path, index=False)
