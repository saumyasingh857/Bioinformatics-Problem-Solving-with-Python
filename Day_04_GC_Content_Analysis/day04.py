# ============================================================
# Bioinformatics Problem Solving with Python
# Episode 04: GC Content Analysis Using Functions
# ============================================================

# ============================================================
# Workflow 1: Read DNA Sequences
# ============================================================

sequence_file = "data/dna_sequences.txt"

with open(sequence_file, "r") as file:
    sequences = file.readlines()

print("=" * 60)
print("GC CONTENT ANALYSIS")
print("=" * 60)

print(f"Total Sequences Loaded: {len(sequences)}")


# ============================================================
# Workflow 2: Create a Reusable GC Content Function
# ============================================================

def calculate_gc_content(sequence):
    """Calculate the GC content percentage of a DNA sequence."""

    sequence = sequence.upper()

    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_content = ((g_count + c_count) / len(sequence)) * 100

    return gc_content
# ============================================================
# Workflow 3: Analyze Each DNA Sequence
# ============================================================

print("\n" + "=" * 60)
print("GC CONTENT RESULTS")
print("=" * 60)

for index, sequence in enumerate(sequences, start=1):

    sequence = sequence.strip().upper()

    gc_content = calculate_gc_content(sequence)

    print(f"Sequence {index}: {gc_content:.2f}%")
    # ============================================================
# Workflow 4: GC Content Classification
# ============================================================

def classify_gc_content(gc_content):

    if gc_content < 40:
        return "Low GC"
    elif gc_content <= 60:
        return "Moderate GC"
    else:
        return "High GC"


print("\n" + "=" * 60)
print("GC CONTENT CLASSIFICATION")
print("=" * 60)

for index, sequence in enumerate(sequences, start=1):

    sequence = sequence.strip().upper()

    gc_content = calculate_gc_content(sequence)
    classification = classify_gc_content(gc_content)

    print(
        f"Sequence {index}: "
        f"{gc_content:.2f}% → {classification}"
    )
 # ============================================================
# Workflow 5: Final GC Content Report
# ============================================================

print("\n" + "=" * 60)
print("FINAL GC CONTENT REPORT")
print("=" * 60)

for index, sequence in enumerate(sequences, start=1):

    sequence = sequence.strip().upper()

    gc_content = calculate_gc_content(sequence)
    classification = classify_gc_content(gc_content)

    print(f"\nSequence {index}")
    print(f"Length         : {len(sequence)} bp")
    print(f"GC Content     : {gc_content:.2f}%")
    print(f"Classification : {classification}")
    
