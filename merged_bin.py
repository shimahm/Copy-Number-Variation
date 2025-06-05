import pandas as pd
import os

# Define chromosome data
chromosomes = {
    'A01': 32958928,
    'A02': 33432960,
    'A03': 39685748,
    'A04': 23101715,
    'A05': 42112164,
    'A06': 45146386,
    'A07': 29390523,
    'A08': 26309499,
    'A09': 53549826,
    'A10': 20778245,
    'C01': 48239358,
    'C02': 62297340,
    'C03': 73669886,
    'C04': 65837619,
    'C05': 56382805,
    'C06': 50218839,
    'C07': 55656957,
    'C08': 41681856,
    'C09': 66465249
}

# Initialize dataframe for bins
bins = []

# Generate bins for each chromosome
for chr_name, length in chromosomes.items():
    start = 1
    while start <= length:
        end = min(start + 999999, length)
        bins.append([chr_name, start, end])
        start += 1000000

# Convert to DataFrame
df_bins = pd.DataFrame(bins, columns=['chr', 'start', 'end'])

# Read and process each sample file
for i in range(1, 19):
    filename = f"s_{str(i).zfill(2)}.txt"
    if os.path.exists(filename):
        df_sample = pd.read_csv(filename, sep='\t')
        cnv_column = []
        for _, row in df_bins.iterrows():
            chr = row['chr']
            start = row['start']
            end = row['end']
            overlapping_cnvs = df_sample[(df_sample['chr'] == chr) &
                                         (df_sample['start'] <= end) &
                                         (df_sample['end'] >= start)]
            if not overlapping_cnvs.empty:
                cnv_column.append(','.join(overlapping_cnvs['cnv'].unique()))
            else:
                cnv_column.append('0') # No CNV
        df_bins[f'sample_{i}'] = cnv_column

# Save to file
df_bins.to_csv('merged_chromosome_bins.csv', index=False)

print("File 'merged_chromosome_bins.csv' has been created.")

