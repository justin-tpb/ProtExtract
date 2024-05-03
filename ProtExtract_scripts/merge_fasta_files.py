from Bio import SeqIO
from natsort import natsorted
import os
import sys

# This script was written for ProtExtract
# It merges FASTA files within a folder into a single FASTA file
# It adds the filename to the front of each sequence header within the file
# Use this with "python3 merge_fasta_files.py <input_dir> <output_file>"

# Check if there are three command-line arguments (the script name counts as an argument)
if len(sys.argv) != 3:
    print("Usage: python3 merge_fasta_files.py <input_dir> <output_file>")
    sys.exit(1)

# Get input folder and output file paths from command line arguments
input_dir = sys.argv[1]
output_file = sys.argv[2]

# Create a list to store the sequences
records = []

# Loop through all files in input directory
for file_name in os.listdir(input_dir):

    # Check if file is a fasta file
    if file_name.endswith((".fasta", ".fa")):

        # Open fasta file for reading
        with open(os.path.join(input_dir, file_name), "r") as input:

            # Parse fasta sequences from file
            for record in SeqIO.parse(input, "fasta"):

                # Add filename without file extension to sequence header
                gene_record = record[:]    # [:] makes a shallow copy
                gene_record.id = file_name.rsplit(".", 1)[0] + "|" + record.id
                gene_record.description = ""
                records.append(gene_record)

# Sort the records based on their header alphabetically and case-insensitive
sorted_records = natsorted(records, key=lambda record: record.id.lower())

# Write sequence to output file
SeqIO.write(sorted_records, output_file, "fasta")
