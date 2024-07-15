#!/bin/bash

specific_file_names="False.tsv true.tsv"

# Create a new folder to move the selected files into
new_folder="/Users/calvincornell/combined"
mkdir -p "${new_folder}"

# Loop through each specific file name
for file_name in ${specific_file_names}; do
    # Use find to locate the file and move it into the new folder
    find "${file_dir}" -maxdepth 1 -type f -name "${file_name}" -exec mv -t "${new_folder}" {} +
done