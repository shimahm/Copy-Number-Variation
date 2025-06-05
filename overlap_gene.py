import pandas as pd

# Load bin CNV data
bins = pd.read_csv("updated_merged_chromosome_bins.csv")

# Load gene annotation data
genes = pd.read_csv("annotated_genes_plot.txt", sep="\t", header=None,
                    names=["chr", "start", "end", "gene_name", "arabidopsis_id"])

# Ensure correct data types
bins['start'] = bins['start'].astype(int)
bins['end'] = bins['end'].astype(int)
genes['start'] = genes['start'].astype(int)
genes['end'] = genes['end'].astype(int)

# List of sample columns
sample_cols = [col for col in bins.columns if col.startswith('sample_')]

# Storage for long-format output
records = []

# For each gene, find matching bin(s)
for idx, gene in genes.iterrows():
    gene_chr = gene['chr']
    gene_start = gene['start']
    gene_end = gene['end']
    gene_name = gene['gene_name']

    # Get bins that fully contain the gene
    matching_bins = bins[
        (bins['chr'] == gene_chr) &
        (bins['start'] <= gene_start) &
        (bins['end'] >= gene_end)
    ]

    if matching_bins.empty:
        # Optional: Skip or add "not_found" value
        continue

    for sample in sample_cols:
        statuses = matching_bins[sample].unique()
        if len(statuses) == 1:
            final_status = statuses[0]
        else:
            final_status = "mixed"
        records.append((gene_name, sample, final_status))

# Create long-format dataframe
result_df = pd.DataFrame(records, columns=["gene_name", "sample", "CNV_status"])

# Save output
result_df.to_csv("gene_cnv_status_long_format.csv", index=False)
print("✔ Done! Output saved to gene_cnv_status_long_format.csv")

