# Explanation

This project uses Python functions to analyze the GC content of multiple DNA sequences.

## Workflow

### 1. Read DNA Sequences
The program loads multiple DNA sequences from a text file.

### 2. Calculate GC Content
The `calculate_gc_content()` function counts G and C bases and calculates their percentage.

### 3. Classify GC Content
The `classify_gc_content()` function categorizes each sequence as:

- Low GC: < 40%
- Moderate GC: 40–60%
- High GC: > 60%

### 4. Generate Report
For each sequence, the program reports:

- Sequence length
- GC content
- GC classification

## Python Concepts

- Functions
- Parameters
- Return values
- String methods
- Loops
- Conditional statements
- File handling

## Biological Significance

GC content provides information about DNA composition and can be useful in genome characterization, comparative genomics, and other sequence-analysis applications.