Copy Number Variation (CNV) analysis in the oil-related genes region of Brassica napus
Overview
This project investigates the genetic basis of fatty acid diversity in Brassica napus by analyzing copy number variations (CNVs), with a focus on the FAE1 gene region. We resequenced 18 selected lines with varying fatty acid levels and implemented a bioinformatics pipeline to identify CNVs contributing to phenotypic variation.

📊 Pipeline Summary
1. Sample Selection and Sequencing
18 plant lines with diverse fatty acid profiles were selected.

Genomic DNA libraries were constructed and subjected to Illumina resequencing.

2. Preprocessing and Quality Control
FastQC: Initial quality check of raw reads.

Trimmomatic: Trimming of low-quality reads and adapter sequences.

FastQC: Re-evaluation to confirm quality improvement.

3. Read Alignment
Trimmed reads were aligned to the Brassica napus reference genome (Darmor-bzh v10) using BWA-MEM.

4. Alignment Refinement
SAM files converted to sorted BAM using samtools.

Reads filtered to retain:

Only uniquely mapped reads (no XA:Z: or SA:Z: tags).

Reads with ≤2 mismatches.

5. Coverage and CNV Analysis
samtools depth used to calculate per-base coverage.

Low-coverage positions (<2) were excluded.

Coverage intersected with gene annotations to assess gene-specific CNVs.

CNV visualization highlighted elevated coverage suggesting gene duplications or deletions.

🧬 Genomic CNV Landscape
A chromosome-wide CNV map was generated:

Blue: Deletions

Red: Duplications

Green: Both deletions and duplications in the same region

White: No CNVs detected

These CNV patterns provide insights into genomic rearrangements potentially linked to trait variation and adaptation.
