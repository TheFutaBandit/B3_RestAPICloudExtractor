import pandas as pd
import numpy as np

count = 0

def search_algorithm(input_file, output_file):
    df = pd.read_csv(input_file)

    bug_reports = df[['Bug_ID', 'Bug_Summary', 'Bug_Description']]

    aging_keywords = [
        'race', 'leak', 'memory', 'aging', 'overflow', 'deplet',
        'Overflow', 'NPE', 'null pointer', 'Buffer exhausted',
        'deadlock', 'flush', 'Leak', 'Memory', 'LEAK',
        'MEMORY', 'OVERFLOW', 'null pointer exception'
    ]

    # Join the keywords with word boundaries to match exact words
    pattern = r'\b(?:' + '|'.join(aging_keywords) + r')\b'

    aging_related_bugs = bug_reports[
        bug_reports['Bug_Description'].str.contains(pattern, case=False, na=False)
    ]

    # Ensure drop_duplicates() is called
    aging_related_bugs.drop_duplicates(inplace=True)

    print(aging_related_bugs.shape[0])

    aging_related_bugs.to_csv(output_file, index=False)

input_file = 'dataset/cassandra_Resolved3Less.csv'
output_file = 'dataset/cassandra_ARBIssues_3.csv'

search_algorithm(input_file, output_file)
