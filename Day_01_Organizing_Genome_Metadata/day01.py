# ============================================================
# Bioinformatics Problem Solving with Python
# Day 01 | Organizing Genome Metadata Using Python Variables
# ============================================================

"""
Biological Problem
------------------
A microbiology laboratory has completed the whole-genome sequencing
of Escherichia coli K-12 MG1655.

Before beginning downstream analyses, researchers need to organize
important genome metadata in a structured format.

In this lesson, we will use Python variables and data types
to organize biological information efficiently.
"""
# ============================================================
# Step 1: Store Genome Metadata
# ============================================================

organism = "Escherichia coli"
strain = "K-12"
substrain = "MG1655"

genome_size_bp = 4641652
gene_count = 4288

gc_content = 50.8
# ============================================================
# Step 2: Store Base Composition
# ============================================================

base_composition = {
    "A": 24.7,
    "T": 24.5,
    "G": 25.4,
    "C": 25.4
}
# ============================================================
# Step 3: Create a Genome Record
# ============================================================

genome_record = {
    "Organism": organism,
    "Strain": strain,
    "Substrain": substrain,
    "Genome Size (bp)": genome_size_bp,
    "Gene Count": gene_count,
    "GC Content (%)": gc_content
}
# ============================================================
# Step 4: Display Genome Metadata
# ============================================================

print("=" * 60)
print("        Genome Metadata Summary")
print("=" * 60)

for key, value in genome_record.items():
    if key == "Genome Size (bp)":
        print(f"{key:<20}: {value:,} bp")
    else:
        print(f"{key:<20}: {value}")

print("=" * 60)
# ============================================================
# Step 5: Display Base Composition
# ============================================================

print("\nBase Composition (%)")
print("-" * 30)

for base, percentage in base_composition.items():
    print(f"{base} : {percentage}%")
    # ============================================================
# Step 6: Biological Interpretation
# ============================================================

print("\nBiological Interpretation")
print("-" * 30)

print(
    f"The genome of {organism} {strain} {substrain} "
    f"contains approximately {gene_count:,} genes "
    f"distributed across a genome of {genome_size_bp:,} base pairs."
)

print(
    f"A GC content of {gc_content}% provides important information "
    "about genome composition and is commonly used in comparative "
    "genomics and molecular biology."
)