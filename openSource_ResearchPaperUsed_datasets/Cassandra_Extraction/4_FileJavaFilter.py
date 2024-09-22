import pandas as pd

# Load the CSV file
df = pd.read_csv('dataset/cassandra_ARBFiles_3.csv')

# Filter the rows where the file column ends with '.java'
df_filtered = df[df['File'].str.endswith('.java')]

# Group by 'File' (file column) and aggregate the 'Bug ID's, joining them with a comma
df_grouped = df_filtered.groupby('File')['Bug_ID'].apply(lambda x: ','.join(x.astype(str))).reset_index()

# Save the grouped dataframe to a new CSV file
df_grouped.to_csv('dataset/cassandra_ARBFiles_3_JavaFilter_Grouped.csv', index=False)
