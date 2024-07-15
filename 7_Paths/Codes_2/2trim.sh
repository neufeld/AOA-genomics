#!/bin/bash

for file in *.tsv; do
  tail -n +4 "$file" > "${file%.tsv}_trimmed.tsv"
done
