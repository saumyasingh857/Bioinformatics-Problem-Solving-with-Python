# Explanation

This project analyzes the nucleotide composition of multiple DNA sequences using Python dictionaries.

## Workflow

### 1. Read DNA Sequences
The program loads multiple sequences from a text file.

### 2. Count Nucleotides
The `count_nucleotides()` function stores the counts of A, T, G, and C in a dictionary.

### 3. Calculate Percentages
The frequency of each nucleotide is converted into a percentage of the total sequence length.

### 4. Identify the Dominant Base
Python's `max()` function is used to identify the nucleotide with the highest count.

### 5. Generate Final Report
For each sequence, the program reports:

- Sequence length
- A count
- T count
- G count
- C count
- Dominant nucleotide

## Python Concepts

- Dictionaries
- Functions
- Loops
- Conditional statements
- `max()`
- String methods
- File handling

## Biological Significance

Nucleotide composition provides information about the characteristics of DNA sequences and can be useful when comparing genomic regions or different organisms.