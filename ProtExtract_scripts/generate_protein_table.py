import os
import csv
import sys

# This script was written for ProtExtract
# It generates a TSV table from all summary files combined
# This table contains information about found and missing proteins in the proteomes
# Use this with "python3 generate_protein_table.py <input_folder> <output_file>"

# Check if there are three command-line arguments (the script name counts as an argument)
if len(sys.argv) != 3:
    print("Usage: python3 generate_protein_table.py <input_folder> <output_file>")
    sys.exit(1)

# Get input folder and output file paths from command line argument
input_folder = sys.argv[1]
output_file = sys.argv[2]

# Get a list of all files in the input folder, sorted alphabetically and case-insensitive
files = sorted(os.listdir(input_folder), key=str.lower)

# Initialize a dictionary to store the protein information
protein_info = {}

# Process each file
for file in files:
    file_path = os.path.join(input_folder, file)
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
        # Read each line and store the protein information in the dictionary
        for line in lines:
            protein, status = line.strip().split()
            protein_info.setdefault(protein, []).append(status)

# Generate the output TSV file
with open(output_file, 'w') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    
    # Write the header row
    header_row = [''] + files
    writer.writerow(header_row)
    
    # Write the protein information rows
    for protein, statuses in protein_info.items():
        row = [protein] + [0 if status == 'missing' else 1 for status in statuses]
        writer.writerow(row)
