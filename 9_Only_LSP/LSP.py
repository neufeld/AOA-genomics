import pandas as pd

def calculate_metrics(filepath, keyword_col_name, keyword, start_col, end_col):
    # Read the Excel file and initialize df
    df = pd.read_excel(filepath, engine='openpyxl')
    
    # Create a new DataFrame to store the results
    results_df = pd.DataFrame(columns=['Column', 'Precision', 'Sensitivity', 'F1'])
    
    # Locate the column containing the keyword
    if keyword_col_name not in df.columns:
        print(f"Error: The specified keyword column '{keyword_col_name}' does not exist in the Excel file.")
        return
    
    keyword_col = df[keyword_col_name]
    
    # Find the rows that contain the specified keyword
    matching_rows = keyword_col[keyword_col == keyword].index.tolist()
    
    if len(matching_rows) == 0:
        print(f"No rows found containing the keyword '{keyword}' in the column '{keyword_col_name}'.")
        return
    
    # Determine the range of rows to include
    range_start = matching_rows[0]
    range_end = matching_rows[-1]
    
    # Loop through the columns in the specified range
    for col in df.columns[start_col:end_col + 1]:
        # Convert the specified range to numeric, coercing non-numeric values to NaN
        range_data = pd.to_numeric(df[col].iloc[range_start:range_end + 1], errors='coerce')
        
        # Calculate precision
        range_sum = range_data.sum(skipna=True)
        range_count = range_data.count()  # Count non-NaN values
        
        print(f"Column: {col}")
        print(f"Range Data: {range_data.tolist()}")
        print(f"Range Sum: {range_sum}")
        print(f"Range Count: {range_count}")
        
        if range_count > 0:
            precision = range_sum / range_count
        else:
            precision = float('nan')
        
        print(f"Precision: {precision}")
        
        # Calculate sensitivity
        total_col_sum = pd.to_numeric(df[col], errors='coerce').sum(skipna=True)
        
        print(f"Total Column Sum: {total_col_sum}")
        
        if total_col_sum != 0:
            sensitivity = range_sum / total_col_sum
        else:
            sensitivity = float('nan')
        
        print(f"Sensitivity: {sensitivity}")
        
        # Calculate F1 score
        if precision + sensitivity > 0:
            f1 = 2 * (precision * sensitivity) / (precision + sensitivity)
        else:
            f1 = float('nan')
        
        print(f"F1 Score: {f1}")
        
        # Create a DataFrame with the current column's results
        new_data = pd.DataFrame({
            'Column': [col],
            'Precision': [precision],
            'Sensitivity': [sensitivity],
            'F1': [f1]
        })
        
        # Concatenate new_data with results_df
        results_df = pd.concat([results_df, new_data], ignore_index=True)
    
    # Save the results DataFrame to a new Excel file
    results_df.to_excel('results.xlsx', index=False)

# Main script
filepath = '/Users/calvincornell/Adj_LSP/adj_peptidase.xlsx'

# Read the Excel file to initialize df
df = pd.read_excel(filepath, engine='openpyxl')

# Calculate end_col using df after initializing it
end_col = len(df.columns) - 1  # Ending column index (0-based)

# Define the column name and keyword to search for
keyword_col_name = 'Group'  # Replace with your keyword column name
keyword = 'ThAOA'  # Replace with your keyword

# Define start_col and end_col (column range)
start_col = 2  # Starting column index (0-based)

# Call the function to calculate metrics
calculate_metrics(filepath, keyword_col_name, keyword, start_col, end_col)
