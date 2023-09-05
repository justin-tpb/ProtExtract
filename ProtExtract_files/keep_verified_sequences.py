from Bio import SeqIO
import sys

# This script was written for ProtExtract
# It keeps sequences from a FASTA file based on strings found in the header
# It needs an input FASTA file and a list of strings for keeping (one string per line)
# Use this with "python3 keep_verified_sequences.py <input_file> <keep_strings_list> <output_file>"
# "keep_strings_list" can be a file or stdin (-)

# Check if there are four command-line arguments (the script name counts as an argument)
if len(sys.argv) != 4:
    print("Usage: python3 keep_verified_sequences.py <input_file> <keep_strings_list> <output_file>")
    sys.exit(1)

# Get the input file, keep strings list, and output file paths from command-line arguments
input_file = sys.argv[1]
keep_strings_list = sys.argv[2]
output_file = sys.argv[3]

# Handle "keep_strings_list" as either stdin or file
if sys.argv[2] == "-":
    keep_strings_list = sys.stdin
    close_file = False
else:
    keep_strings_list = open(keep_strings_list, "r")
    close_file = True

# Create a list to store the strings to keep
keep_strings = []

# Read the strings to keep from the keep strings list and append "|"
with keep_strings_list as file:
    for line in file:
        keep_strings.append(line.strip() + "|")

# Close "keep_strings_list" if it is a file
if close_file:
    keep_strings_list.close()

# Create a list to store the sequences to keep
kept_records = []

# Loop through each sequence in the input FASTA file
for record in SeqIO.parse(input_file, "fasta"):
    if any(string in record.id for string in keep_strings):
        kept_records.append(record)

# Write the filtered sequences to the output FASTA file
SeqIO.write(kept_records, output_file, "fasta")
