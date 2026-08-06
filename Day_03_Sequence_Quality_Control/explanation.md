# 📘 Explanation

This project demonstrates how Python loops and conditional statements can automate DNA sequence quality control.

## Workflow

### 1. Read DNA Sequences
The program loads multiple DNA sequences from a text file.

### 2. Display Sequences
Each sequence is displayed with its sequence number.

### 3. Sequence Length Check
Sequences shorter than 10 base pairs are classified as low quality.

### 4. Invalid Nucleotide Detection
Each nucleotide is checked against the valid DNA bases (A, T, G, and C). Sequences containing invalid characters are rejected.

### 5. Final QC Classification
Each sequence is classified as:
- PASS
- FAIL (Too Short)
- FAIL (Invalid Nucleotide)

### 6. QC Summary
The program calculates:
- Total sequences
- Passed sequences
- Failed sequences
- Pass rate

### 7. Biological Interpretation
The final report explains why quality control is important before downstream bioinformatics analyses such as sequence alignment, genome assembly, and variant calling.