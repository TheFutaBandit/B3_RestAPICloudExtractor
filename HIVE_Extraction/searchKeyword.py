import pandas as pd

def search_algorithm(input_file, output_file):
    df = pd.read_csv(input_file)

    bug_reports = df[['Bug_ID','Bug_Summary','Bug_Description']]

    aging_keywords = [
        'race', 'leak', 'memory', 'aging', 'overflow', 'deplet', 
        'Overflow', 'NPE', 'null pointer', 'Buffer exhausted', 
        'deadlock', 'flush', 'Leak', 'Memory', 'LEAK', 
        'MEMORY', 'OVERFLOW', 'null pointer exception'
    ]

    aging_related_bugs = bug_reports[
        bug_reports['Bug_Summary'].str.contains('|'.join(aging_keywords),case=False, na=False)
    ]

    aging_related_bugs.drop_duplicates

    aging_related_bugs.to_csv(output_file, index=False)

input_file = 'dataset/HIVE_Closed_3.csv'
output_file = 'dataset/HIVE_ARBIssues_3.csv'

search_algorithm(input_file,output_file)