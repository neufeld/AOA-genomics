#!/bin/bash

for file in *_trimmed_iso.tsv; do
  file_name=$(basename "$file" .tsv)
  temp_file=$(mktemp)

  # Using awk to change the column names
  awk -v col_name="$file_name" 'BEGIN {FS=OFS="\t"} { if (FNR==1) for (i=1; i<=NF; i++) $i=col_name } 1' "$file" > "$temp_file"

  # Replace the original file with the updated one
  mv "$temp_file" "$file"
done
