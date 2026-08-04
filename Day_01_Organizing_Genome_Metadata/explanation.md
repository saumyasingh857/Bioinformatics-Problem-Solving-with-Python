# 🐍 Python Concepts Explained

## Why Do We Need Variables?

Imagine a researcher trying to remember thousands of genome sizes, gene counts, and organism names.

Instead of memorizing or repeatedly typing these values, Python allows us to store them in **variables**.

A variable is simply a named container that stores information.

Example:

```python
organism = "Escherichia coli"
```

Here, `organism` stores the name of the bacterium.

---

# Data Types Used in This Project

Python automatically recognizes different types of data.

## 1. String (`str`)

Strings store text.

Examples:

- Organism name
- Strain
- Gene symbol
- DNA sequence

Example:

```python
organism = "Escherichia coli"
```

---

## 2. Integer (`int`)

Integers store whole numbers.

Examples:

- Genome size
- Gene count
- Chromosome number

Example:

```python
gene_count = 4288
```

---

## 3. Float (`float`)

Floats store decimal values.

Examples:

- GC Content
- Gene expression values
- Read quality scores

Example:

```python
gc_content = 50.8
```

---

## 4. List (`list`)

Lists store multiple values that can be modified.

Example:

```python
genes = ["lacZ", "lacY", "lacA"]
```

Lists are useful for storing multiple genes, sequences, or samples.

---

## 5. Tuple (`tuple`)

Tuples store multiple values that should not change.

Example:

```python
genome_summary = (
    organism,
    strain,
    gene_count
)
```

Tuples are useful for creating fixed biological records.

---

# Why These Concepts Matter

Almost every bioinformatics pipeline begins by organizing biological information.

Whether you're working with bacterial genomes, RNA-Seq data, or protein sequences, understanding variables and data types is the foundation for writing reliable and reusable Python programs.

---

# Key Takeaway

Today, you learned how Python stores biological information using variables and different data types.

These concepts form the foundation for every bioinformatics workflow you'll build in the future.