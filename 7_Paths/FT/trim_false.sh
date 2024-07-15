#!/bin/bash


file_to_modify="true.tsv"

# Create a temporary file to store the modified content
temp_file=$(mktemp)

# Use tail to remove the first two rows from the file and save the result to the temporary file
tail -n +3 "${file_to_modify}" > "${temp_file}"

# Move the modified content back to the original file
mv "${temp_file}" "${file_to_modify}"