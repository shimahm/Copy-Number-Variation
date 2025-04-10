🧬 Copy Number Variation (CNV) Analysis in the FA Gene Region of Brassica napus
🔍 Overview
This project explores the genetic basis of fatty acid diversity in Brassica napus by analyzing Copy Number Variations (CNVs)—with a special focus on the FAE1 gene region.
We resequenced 18 lines showing variation in fatty acid content and implemented a robust bioinformatics pipeline to detect CNVs potentially driving phenotypic differences.

⚙️ Pipeline Summary
1️⃣ Sample Selection & Resequencing
Constructed genomic DNA libraries from selected lines.

Performed Illumina paired-end sequencing.

2️⃣ Preprocessing & Quality Control
🔹 FastQC: Initial quality assessment of raw reads

🔹 Trimmomatic: Trimmed low-quality bases and adapter sequences

🔹 FastQC: Rechecked for improved quality post-trimming

3️⃣ Read Alignment
🧬 Aligned clean reads to the Brassica napus reference genome (Darmor-bzh v10) using BWA-MEM

4️⃣ Alignment Refinement
🔸 Converted SAM → sorted BAM with samtools

🔸 Applied filtering to retain:

✅ Uniquely mapped reads (excluding XA:Z: or SA:Z: tags)

✅ Reads with ≤ 2 mismatches

5️⃣ Coverage Calculation & CNV Detection
📏 Calculated per-base coverage depth with samtools depth

❌ Excluded positions with coverage < 2

🧠 Intersected coverage data with gene annotations

📊 Visualized coverage to detect CNVs (e.g., elevated or reduced depth in FAE1 region)

🌍 CNV Landscape Across the Genome
A genome-wide CNV map was generated with color-coded segments representing 1 Mbp regions:

Color	Interpretation
🔵 Blue	Deletions
🔴 Red	Duplications
🟢 Green	Both duplications and deletions
⚪ White	No CNVs detected

🧩 These patterns highlight regions of structural variation that may be associated with trait diversity and adaptive potential in Brassica napus.
