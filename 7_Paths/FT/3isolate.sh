#!/bin/bash

tsv_files=$(ls *_trimmed.tsv)

# Loop through each .tbl file and convert it to .tsv using awk

for file in $tsv_files; do

cut -f 3 "$file" > "${file%.tsv}_iso.tsv"

done