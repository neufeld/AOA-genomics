import os
import pandas as pd

def search_and_extract(input_folder, output_folder, keyword_list):
    for filename in os.listdir(input_folder):
        if filename.endswith(".xlsx"):
            input_filepath = os.path.join(input_folder, filename)
            output_filepath_prefix = os.path.join(output_folder, os.path.splitext(filename)[0])

            # Read the original Excel file
            df = pd.read_excel(input_filepath)

            for keyword in keyword_list:
                # Create a new DataFrame with rows containing the keyword
                filtered_df = df[df.apply(lambda row: any(keyword.lower() in str(cell).lower() for cell in row), axis=1)]

                # Save the filtered DataFrame to a new Excel file
                output_filepath = f"{output_filepath_prefix}_{keyword}.xlsx"
                filtered_df.to_excel(output_filepath, index=False)

if __name__ == "__main__":
    # Replace these paths and keywords with your own values
    input_folder_path = '/Users/calvincornell/poster/'
    output_folder_path = '/Users/calvincornell/poster/output'
    keywords_to_search = ["Ammonia", "NADPH", "CO2", "ATP", "CTP", "GTP","TTP","CoA", "NADH","FADH2","Quinone", "Ferricytochrome", "FADH2"]

    search_and_extract(input_folder_path, output_folder_path, keywords_to_search)
