import pandas as pd

# Load the data
df = pd.read_csv('merged_chromosome_bins.csv')

# Function to classify CNVs
def classify_cnv(row):
    deletions = ['del', 'miss']
    duplications = ['dup', 'gain']
    deletion_count = sum(row[f'sample_{i}'] in deletions for i in range(1, 19))
    duplication_count = sum(row[f'sample_{i}'] in duplications for i in range(1, 19))
    
    if deletion_count > 0 and duplication_count > 0:
        return 'dup/del'
    elif deletion_count > 0:
        return 'deletion'
    elif duplication_count > 0:
        return 'duplication'
    else:
        return 'no CNV'

# Apply the classification function
df['CNV_Group'] = df.apply(classify_cnv, axis=1)

# Count the number of samples with CNVs
df['CNV_Count'] = df.apply(lambda row: sum(row[f'sample_{i}'] != '0' for i in range(1, 19)), axis=1)

# Save the updated dataframe to a new CSV file
df.to_csv('updated_merged_chromosome_bins.csv', index=False)

