# ============================================================
# Bioinformatics Problem Solving with Python
# Episode 05: Nucleotide Composition Analysis
# ============================================================

# ============================================================
# Workflow 1: Read DNA Sequences
# ============================================================

sequence_file = "data/dna_sequences.txt"

with open(sequence_file, "r") as file:
    sequences = file.readlines()

print("=" * 60)
print("NUCLEOTIDE COMPOSITION ANALYSIS")
print("=" * 60)

print(f"Total Sequences Loaded: {len(sequences)}")


# ============================================================
# Workflow 2: Count Nucleotides Using a Dictionary
# ============================================================

def count_nucleotides(sequence):

    nucleotide_counts = {
        "A": 0,
        "T": 0,
        "G": 0,
        "C": 0
    }

    for base in sequence:
        if base in nucleotide_counts:
            nucleotide_counts[base] += 1

    return nucleotide_counts
# ============================================================
# Workflow 3: Analyze Each Sequence
# ============================================================

print("\n" + "=" * 60)
print("NUCLEOTIDE COUNTS")
print("=" * 60)

for index, sequence in enumerate(sequences, start=1):

    sequence = sequence.strip().upper()

    counts = count_nucleotides(sequence)

    print(f"\nSequence {index}")
    print(f"A : {counts['A']}")
    print(f"T : {counts['T']}")
    print(f"G : {counts['G']}")
    print(f"C : {counts['C']}")
 # ============================================================
# Workflow 4: Calculate Nucleotide Percentages
# ============================================================

print("\n" + "=" * 60)
print("NUCLEOTIDE COMPOSITION (%)")
print("=" * 60)

for index, sequence in enumerate(sequences, start=1):

    sequence = sequence.strip().upper()

    counts = count_nucleotides(sequence)
    total_bases = len(sequence)

    print(f"\nSequence {index}")

    for base, count in counts.items():
        percentage = (count / total_bases) * 100
        print(f"{base} : {percentage:.2f}%")
# ============================================================
# Workflow 5: Identify the Most Abundant Nucleotide
# ============================================================

print("\n" + "=" * 60)
print("DOMINANT NUCLEOTIDE")
print("=" * 60)

for index, sequence in enumerate(sequences, start=1):

    sequence = sequence.strip().upper()

    counts = count_nucleotides(sequence)

    dominant_base = max(counts, key=counts.get)

    print(
        f"Sequence {index}: "
        f"{dominant_base} ({counts[dominant_base]} bases)"
    )
# ============================================================
# Workflow 6: Final Composition Report
# ============================================================

print("\n" + "=" * 60)
print("FINAL NUCLEOTIDE COMPOSITION REPORT")
print("=" * 60)

for index, sequence in enumerate(sequences, start=1):

    sequence = sequence.strip().upper()

    counts = count_nucleotides(sequence)
    total_bases = len(sequence)
    dominant_base = max(counts, key=counts.get)

    print(f"\nSequence {index}")
    print(f"Length          : {total_bases} bp")
    print(f"A               : {counts['A']}")
    print(f"T               : {counts['T']}")
    print(f"G               : {counts['G']}")
    print(f"C               : {counts['C']}")
    print(f"Dominant Base   : {dominant_base}")
    