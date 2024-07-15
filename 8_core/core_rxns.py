import pandas as pd
import os

def core_analysis(input_file):
    # Read the input Excel file
    df = pd.read_excel(input_file)

    # Extract the header row for the columns
    headers = df.columns[2:]  # Headers from column 3 onwards are the protein names

    # Find proteins that are present in all species
    # We will check each column (from column 3 onwards) for proteins that are present in all species
    all_present_proteins = []
    
    # Iterate through the headers (protein names)
    for protein in headers:
        # Check if the protein is present (value 1) in all rows (species)
        if df[protein].all():
            # If the protein is present in all species, add it to the list
            all_present_proteins.append(protein)
    
    # Create a DataFrame to hold the output data
    output_df = pd.DataFrame({'Proteins in all species': all_present_proteins})
    
    # Define the output file path
    # The output file will be in the same directory as the input file
    # and have a name like "<input_filename>_core_proteins.xlsx"
    input_file_name, input_file_extension = os.path.splitext(input_file)
    output_file = f"{input_file_name}_core_proteins.xlsx"
    
    # Write the output DataFrame to an Excel file
    output_df.to_excel(output_file, index=False)
    
    print(f"Output written to: {output_file}")

def main():
    # Prompt the user for the input file path or name
    input_file = input("Please enter the name or path of the input .xlsx file: ")
    
    # Perform the core analysis
    core_analysis(input_file)

if __name__ == '__main__':
    main()
