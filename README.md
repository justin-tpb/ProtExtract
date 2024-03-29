# ProtExtract 0.9.0
A Linux command-line tool to extract homologous proteins from proteomes.

## Description

ProtExtract uses DIAMOND to search for homologs of proteins in proteomes and extracts the sequences
with the highest bit-score sums among all alignments with homologuous sequences of a query protein.
It then performs a reciprocal DIAMOND search for verification and only keeps the extracted sequences
which realign with a homologuous sequence of the same query protein as before as final homologs.
The extracted and verified sequences will be annotated with the filename of the homologous protein.
Various information files about the found and missing proteins are created as well, including an output table.


## Input

A directory with protein files as queries, preferably with multiple homologs of the same protein per file for higher accuracy.
	
* The protein filenames will be treated as the protein names and must not contain spaces.
* If any gaps exist within the protein sequences, they will be copied for gap removal.
* The default directory is 'Proteins' and the default file extension is '.fasta'.
* A custom directory can be provided with the option -q and a custom file extension with -Q.
   
A directory with proteome files as subjects. Can be the same input folder, as long as the file extensions are different.

* The sequence headers should ideally not contain vertical bars '|'.
* The default directory is 'Proteomes' and the default file extension is '.fasta'.
* A custom directory can be provided with the option -s and a custom file extension with -S.


## Requirements

Linux or WSL 2 on Windows

'ProtExtract_files' folder in the same directory as ProtExtract containing the following scripts (provided with the tool):
    
    merge_fasta_files.py
    extract_and_rename_sequences.py
    keep_verified_sequences.py
    generate_protein_table.py
Conda environment called 'protextract' with DIAMOND, Python 3, Biopython and natsort installed.

You can create a conda environment automatically using the -c or -C  option or manually install these packages.


## Usage

To use ProtExtract, you must run the following command in the terminal:

    ./ProtExtract [options]


## Options

    -q DIRECTORY: Protein (query) input directory. Defaults to 'Proteins'.
       Add proteins for which homologs are to be extracted here.
    -Q STRING: Protein (query) file extension. Defaults to '.fasta'.
    -s DIRECTORY: Proteome (subject) input directory. Defaults to 'Proteomes'.
       Add proteomes from which proteins are to be extracted here.
    -S STRING: Proteome (subject) file extension. Defaults to '.fasta'.
    -o DIRECTORY: Output directory. Defaults to 'Output'.
    -m STRING: Sensitivity mode for DIAMOND. Defaults to 'very-sensitive'.
       Available modes: 'fast', 'mid-sensitive', 'sensitive', 'more-sensitive', 'very-sensitive', 'ultra-sensitive'
    -E STRING: Maximum allowed E-value for DIAMOND. Defaults to '1e-20'.
    -% INTEGER: Minimum required percentage of query and subject coverage for DIAMOND. Defaults to '50'.
    -p INTEGER: Minimum required percentage of identical positions for DIAMOND. Defaults to '20'.
    -f: Force overwrite of existing output files.
    -c: Create the required conda environment with Anaconda.
    -C: Create the required conda environment with Mamba.
    -v: Display the version number.
    -h: Show the help message.


## Example Usage

To install the required conda environment, navigate to the directory containing the ProtExtract file, enter the following command and follow the instructions:

    ./ProtExtract -c

To run ProtExtract with default options, navigate to the directory containing the ProtExtract file and enter the following command:

    ./ProtExtract

This will run ProtExtract with the default options:

    Proteins (queries): ./Proteins/*.fasta
    Proteomes (subjects): ./Proteomes/*.fasta
    Output directory: ./Output/
    Sensitivity mode: very-sensitive
    Maximum allowed E-value: 1e-20
    Minimum required coverage: 50%
    Minimum required percent identity: 20%

To run ProtExtract with custom options, navigate to the directory containing the ProtExtract.sh file and enter the following command:

    ./ProtExtract -q ./my_proteins/ -Q .fa -s ./my_proteomes/ -S .pep -o ./my_output/ -m fast -E 1e-30 -% 60 -p 50

This will run ProtExtract with the following options:

    Proteins (queries): ./my_proteins/*.fa
    Proteomes (subjects): ./my_proteomes/*.pep
    Output directory: ./my_output/
    Sensitivity mode: fast
    Maximum allowed E-value: 1e-30
    Minimum required coverage: 60%
    Minimum required percent identity: 50%

## Author

  Justin Teixeira Pereira Bassiaridis


## Changelog

    0.1.0: First version. Homologous sequences are identified by lowest E-value.
    0.1.1: Homologous sequences are now identified by highest bit-score, as multiple alignments with an E-value of 0 might exist.
    0.2.0: Added options to provide the input proteins and proteomes, as well as options to show the help menu and the current version.
    0.2.1: Homologous sequences are now identified by highest bit-score sum among all alignments with homologuous sequences of a query protein.
    0.3.0: Added an option to specify an output folder, including an overwrite check and a force overwrite option.
    0.3.1: Added E-value, coverage and percentage identity threshold options for DIAMOND.
    0.4.0: Added options for automatic setup of the required Anaconda environment with Anaconda or Mamba.
    0.4.1: Added query and subject coverage to 12th and 13th column of the output format 6.
    0.5.0: Major feature update: Added reciprocal verification with DIAMOND.
    0.5.1: Fixed a bug which sometimes caused unverified proteins to be kept as final homologs.
    0.6.0: Gaps within query protein sequences will now be removed to improve DIAMOND results.
    0.6.1: Switched to natural sorting of protein names wherever possible.
    0.7.0: A protein summary table containing information about all found and missing proteins in the proteomes is now generated.
    0.7.1: Fixed a bug which caused ProtExtract to crash when no proteins were found at all.
    0.8.0: Added an option to select the sensitivity level of DIAMOND.
    0.8.1: Runtime is now displayed at the end.
    0.9.0: Cleaned up the code. Release version.


# License

    MIT License

    Copyright (c) 2023 Justin Teixeira Pereira Bassiaridis

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
