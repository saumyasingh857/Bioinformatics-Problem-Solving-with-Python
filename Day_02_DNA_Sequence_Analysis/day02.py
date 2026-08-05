# ============================================================
# Bioinformatics Problem Solving with Python
# Episode 02: DNA Sequence Analysis Using Python Strings
# ============================================================

# ============================================================
# Workflow 1: Read DNA Sequence
# ============================================================

sequence_file = "data/ecoli_dna.txt"

with open(sequence_file, "r") as file:
    dna_sequence = file.read().strip().upper()

print("=" * 60)
print("DNA Sequence Successfully Loaded")
print("=" * 60)

print(dna_sequence)
# ============================================================
# Workflow 2: Validate DNA Sequence
# ============================================================

valid_bases = {"A", "T", "G", "C"}

is_valid = True

for base in dna_sequence:
    if base not in valid_bases:
        is_valid = False
        print(f"Invalid nucleotide found: {base}")
        break

if is_valid:
    print("\n✅ DNA sequence validation passed.")
else:
    print("\n❌ DNA sequence validation failed.")
 # ============================================================
# Workflow 3: Calculate Basic Sequence Statistics
# ============================================================

sequence_length = len(dna_sequence)

count_A = dna_sequence.count("A")
count_T = dna_sequence.count("T")
count_G = dna_sequence.count("G")
count_C = dna_sequence.count("C")

print("\n" + "=" * 60)
print("Basic DNA Sequence Statistics")
print("=" * 60)

print(f"Sequence Length : {sequence_length} bp")
print(f"Adenine (A)     : {count_A}")
print(f"Thymine (T)     : {count_T}")
print(f"Guanine (G)     : {count_G}")
print(f"Cytosine (C)    : {count_C}")
# ============================================================
# Workflow 4: Calculate GC Content
# ============================================================

gc_count = count_G + count_C

gc_content = (gc_count / sequence_length) * 100

at_count = count_A + count_T

at_content = (at_count / sequence_length) * 100

print("\n" + "=" * 60)
print("GC Content Analysis")
print("=" * 60)

print(f"GC Count        : {gc_count}")
print(f"AT Count        : {at_count}")
print(f"GC Content      : {gc_content:.2f}%")
print(f"AT Content      : {at_content:.2f}%")
# ============================================================
# Workflow 5: Detect Start and Stop Codons
# ============================================================

start_codon = dna_sequence[:3]
stop_codon = dna_sequence[-3:]

print("\n" + "=" * 60)
print("Start and Stop Codon Analysis")
print("=" * 60)

print(f"Start Codon : {start_codon}")
print(f"Stop Codon  : {stop_codon}")

if start_codon == "ATG":
    print("✅ Valid Start Codon Detected")
else:
    print("❌ No Start Codon Detected")

if stop_codon in ["TAA", "TAG", "TGA"]:
    print("✅ Valid Stop Codon Detected")
else:
    print("❌ No Stop Codon Detected")
# ============================================================
# Workflow 6: DNA to RNA Transcription
# ============================================================

rna_sequence = dna_sequence.replace("T", "U")

print("\n" + "=" * 60)
print("DNA to RNA Transcription")
print("=" * 60)

print(f"DNA : {dna_sequence}")
print(f"RNA : {rna_sequence}")
# ============================================================
# Workflow 7: Scientific Report
# ============================================================

print("\n" + "=" * 60)
print("Scientific Report")
print("=" * 60)

print(f"Sequence Length      : {sequence_length} bp")
print(f"Adenine (A)          : {count_A}")
print(f"Thymine (T)          : {count_T}")
print(f"Guanine (G)          : {count_G}")
print(f"Cytosine (C)         : {count_C}")
print(f"GC Content           : {gc_content:.2f}%")
print(f"AT Content           : {at_content:.2f}%")
print(f"Start Codon          : {start_codon}")
print(f"Stop Codon           : {stop_codon}")

print("\nBiological Interpretation")
print("-" * 60)

print(f"The DNA fragment contains {sequence_length} base pairs.")

print(
    f"The GC content is {gc_content:.2f}%, indicating the proportion "
    "of guanine and cytosine nucleotides in this sequence."
)

if start_codon == "ATG":
    print("The sequence begins with the canonical start codon (ATG).")
else:
    print("No canonical start codon was detected at the beginning of the sequence.")

if stop_codon in ["TAA", "TAG", "TGA"]:
    print("The sequence ends with a valid stop codon.")
else:
    print("The sequence does not end with a standard stop codon.")

print(
    "These analyses provide a basic overview of the sequence before "
    "performing advanced bioinformatics analyses such as sequence alignment, "
    "gene prediction, or genome annotation."
)

    
