#!/bin/bash

# Download the NAVAll.txt file
curl -s https://www.amfiindia.com/spages/NAVAll.txt -o NAVAll.txt

# Output file
OUTPUT="nav_data.tsv"

# Extract Scheme Name (column 4) and NAV (column 5), skipping headers and blank lines
awk -F ';' 'NF >= 5 && $1 ~ /^[0-9]+$/ { print $4 "\t" $5 }' NAVAll.txt > "$OUTPUT"

echo "Saved extracted data to $OUTPUT"

