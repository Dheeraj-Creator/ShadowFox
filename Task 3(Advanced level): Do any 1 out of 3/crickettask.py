import pandas as pd

weights = {
    'CP': 1.0,
    'GT': 1.5,
    'C': 3.0,
    'DC': -2.0,
    'ST': 2.5,
    'RO': 3.0,
    'MRO': -1.5,
    'DH': 2.0
}

def calculate_ps(row):
    return (
        row['CP'] * weights['CP'] +
        row['GT'] * weights['GT'] +
        row['C'] * weights['C'] +
        row['DC'] * weights['DC'] +
        row['ST'] * weights['ST'] +
        row['RO'] * weights['RO'] +
        row['MRO'] * weights['MRO'] +
        row['DH'] * weights['DH'] +
        row['RS']
    )

df = pd.read_csv('sample_fielding_dataset.csv')
df['Performance Score'] = df.apply(calculate_ps, axis=1)
df.to_csv('cricket_fielding_analysis.csv', index=False)
print(df[['Player Name', 'Performance Score']])
