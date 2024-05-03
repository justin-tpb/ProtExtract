from Bio import SeqIO
from natsort import natsorted
import sys

# This script was written for ProtExtract
# It extracts sequences from a FASTA file and adds a string to the header
# It needs an input FASTA file and a file with the strings and sequence headers
# One string and sequence header per line, delimited by space
# Use this with "python3 extract_and_rename_seqs.py <input_file> <list_file> <output_file>"

# Check if there are four command-line arguments (the script name counts as an argument)
if len(sys.argv) != 4:
    print("Usage: python3 extract_and_rename_seqs.py <input_file> <list_file> <output_file>")
    sys.exit(1)

# Get input folder, list file and output file paths from command line arguments
input_file = sys.argv[1]
list_file = sys.argv[2]
output_file = sys.argv[3]

# Create a dictionary to store the sequence headers and their associated strings
sequences = {}

# Read in the list file and populate a dictionary
with open(list_file, 'r') as list:
    for line in list:
        parts = line.split()
        string_id = parts[0]
        sequence_id = parts[1]
        sequences.setdefault(sequence_id, []).append(string_id)

# Create a list to store the sequences
records = []

# Read in the input file and extract the sequences for the genes
for record in SeqIO.parse(input_file, "fasta"):
    if record.id in sequences:
        for sequence_id in sequences[record.id]:
            sequence_record = record[:]    # [:] makes a shallow copy
            sequence_record.id = f"{sequence_id}|{record.id}"
            sequence_record.description = ""
            records.append(sequence_record)

# Sort the records based on their header alphabetically and case insensitive
sorted_records = natsorted(records, key=lambda record: record.id.lower())

# Write the sorted records to the output fasta file
SeqIO.write(sorted_records, output_file, "fasta")
