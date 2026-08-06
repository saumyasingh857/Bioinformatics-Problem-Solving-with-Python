# ============================================================
# Bioinformatics Problem Solving with Python
# Episode 03: Sequence Quality Control
# ============================================================

# ============================================================
# Workflow 1: Read DNA Sequences
# ============================================================

sequence_file = "data/dna_sequences.txt"

with open(sequence_file, "r") as file:
    sequences = file.readlines()

print("=" * 60)
print("DNA Sequences Successfully Loaded")
print("=" * 60)

print(f"Total Sequences Loaded: {len(sequences)}")
# ============================================================
# Workflow 2: Display Each Sequence
# ============================================================

print("\n" + "=" * 60)
print("Sequences")
print("=" * 60)

for index, sequence in enumerate(sequences, start=1):
    sequence = sequence.strip().upper()
    print(f"Sequence {index}: {sequence}")
 # ============================================================
# Workflow 3: Sequence Length Quality Check
# ============================================================

print("\n" + "=" * 60)
print("Sequence Length Quality Check")
print("=" * 60)

minimum_length = 10

for index, sequence in enumerate(sequences, start=1):

    sequence = sequence.strip().upper()

    sequence_length = len(sequence)

    print(f"\nSequence {index}")
    print(f"Length : {sequence_length} bp")

    if sequence_length >= minimum_length:
        print("✅ PASS : Sequence length is acceptable.")
    else:
        print("⚠ FAIL : Sequence is too short.")
 # ============================================================
# Workflow 4: Detect Invalid Nucleotides
# ============================================================

print("\n" + "=" * 60)
print("Invalid Nucleotide Detection")
print("=" * 60)

valid_bases = {"A", "T", "G", "C"}

for index, sequence in enumerate(sequences, start=1):

    sequence = sequence.strip().upper()

    invalid_found = False

    for base in sequence:

        if base not in valid_bases:

            print(f"\nSequence {index}")
            print(f"Invalid nucleotide detected: {base}")

            invalid_found = True
            break

    if not invalid_found:
        print(f"\nSequence {index}")
        print("No invalid nucleotides found.")
 # ============================================================
# Workflow 5: Final QC Classification
# ============================================================

print("\n" + "=" * 60)
print("Final Quality Control Report")
print("=" * 60)

valid_bases = {"A", "T", "G", "C"}
minimum_length = 10

for index, sequence in enumerate(sequences, start=1):

    sequence = sequence.strip().upper()

    if len(sequence) < minimum_length:
        print(f"Sequence {index}: ❌ FAIL (Too Short)")
        continue

    invalid = False

    for base in sequence:
        if base not in valid_bases:
            print(f"Sequence {index}: ❌ FAIL (Invalid Base: {base})")
            invalid = True
            break

    if not invalid:
        print(f"Sequence {index}: ✅ PASS")
# ============================================================
# Workflow 6: QC Summary Report
# ============================================================

total_sequences = len(sequences)
passed = 0
failed = 0

valid_bases = {"A", "T", "G", "C"}
minimum_length = 10

for sequence in sequences:

    sequence = sequence.strip().upper()

    if len(sequence) < minimum_length:
        failed += 1
        continue

    invalid = False

    for base in sequence:
        if base not in valid_bases:
            invalid = True
            break

    if invalid:
        failed += 1
    else:
        passed += 1

print("\n" + "=" * 60)
print("QC Summary")
print("=" * 60)

print(f"Total Sequences : {total_sequences}")
print(f"Passed          : {passed}")
print(f"Failed          : {failed}")
print(f"Pass Rate       : {(passed/total_sequences)*100:.2f}%")
# ============================================================
# Workflow 7: Biological Interpretation
# ============================================================

print("\n" + "=" * 60)
print("Biological Interpretation")
print("=" * 60)

print(
    f"Out of {total_sequences} DNA sequences, "
    f"{passed} passed the quality-control checks "
    f"while {failed} failed."
)

print(
    "Sequences that are too short or contain invalid "
    "nucleotides should be removed before downstream "
    "bioinformatics analyses."
)

print(
    "Quality control is an essential preprocessing step "
    "before sequence alignment, genome assembly, variant "
    "calling, and gene prediction."
)
