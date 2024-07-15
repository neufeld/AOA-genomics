#!/bin/bash

output_file="combined_columns.tsv"

# Remove the output file if it already exists
rm -f "$output_file"

for file in *_trimmed_iso.tsv; do
  cut -f 2 "$file" > "${file%.tsv}_column2.txt"
done

paste *_column2.txt > "$output_file"

# Clean up temporary files
rm *_column2.txt
