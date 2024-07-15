import os
import pandas as pd

# Prompt the user to enter the full path to the input directory
input_folder = input("Please enter the full path to the input directory: ")

# Define the output directory inside the input directory
output_folder = os.path.join(input_folder, "filtered_files")

# Create the output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over each file in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an Excel file
    if filename.endswith(".xlsx"):
        # Construct the full file path
        input_file_path = os.path.join(input_folder, filename)
        
        try:
            # Read the Excel file into a DataFrame
            # Assuming default sheet and no headers
            df = pd.read_excel(input_file_path, header=None)

            # Extract the prefix from the filename (characters to the left of the first dash)
            prefix = filename.split('-')[0] if '-' in filename else filename.rsplit('.', 1)[0]

            # Prepend the prefix to each phrase in column A (index 0)
            df.iloc[:, 0] = prefix + df.iloc[:, 0].astype(str)

            # Filter rows where the second column (index 1) is not empty
            filtered_df = df[df.iloc[:, 1].notnull()]

            # Define the output file path
            output_file_path = os.path.join(output_folder, filename)

            # Save the filtered DataFrame as a new .xlsx file
            filtered_df.to_excel(output_file_path, index=False, header=False)
        
        except Exception as e:
            print(f"An error occurred while processing {filename}: {e}")

print("All files have been processed and saved to the output folder.")
