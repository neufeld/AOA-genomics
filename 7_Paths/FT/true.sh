#!/bin/bash

search_word="true"

output_file="true.tsv"

# Loop through each file in the directory
for file in "${file_dir}"*; do
    echo "Counts for ${file}:" >> "${output_file}"

    # Use awk to iterate through each column and grep to count occurrences of the word in each column
    awk -v word="${search_word}" '{ for (i = 1; i <= NF; i++) if ($i == word) count[i]++ } END { for (i = 1; i <= NF; i++) print "Column " i ": " count[i] }' "${file}" >> "${output_file}"

    echo >> "${output_file}"
done