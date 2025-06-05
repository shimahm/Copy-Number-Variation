import pandas as pd

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

# Initialize dataframe
bins = []

# Generate bins for each chromosome
for chr_name, length in chromosomes.items():
    start = 1
    while start <= length:
        end = min(start + 999999, length)
        bins.append([chr_name, start, end])
        start += 1000000

# Convert to DataFrame
df = pd.DataFrame(bins, columns=['chr', 'start', 'end'])

# Save to file
df.to_csv('chromosome_bins.csv', index=False)

print("File 'chromosome_bins.csv' has been created.")

