#!/bin/bash

# Get a list of .tbl files in the current directory
tbl_files=$(ls *.tbl)

# Loop through each .tbl file and convert it to .tsv using awk
for file in $tbl_files; do
    awk -F'\t' -v OFS='\t' '{ $1=$1 } 1' "$file" > "${file%.tbl}.tsv"
done
