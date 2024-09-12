import pandas as pd

def search_algorithm(input_file, output_file):
    df = pd.read_csv(input_file)

   
    bug_reports = df[['Bug ID', 'Bug Summary', 'Bug Description']]


    aging_keywords = [
        'race', 'leak', 'memory', 'aging', 'overflow', 'deplet', 
        'Overflow', 'NPE', 'null pointer', 'Buffer exhausted', 
        'deadlock', 'flush', 'Leak', 'Memory', 'LEAK', 
        'MEMORY', 'OVERFLOW', 'null pointer exception'
    ]


    aging_related_bugs = bug_reports[
        bug_reports['Bug Description'].str.contains('|'.join(aging_keywords), case=False, na=False)
    ]

    aging_related_bugs = aging_related_bugs.drop_duplicates()

    
    aging_related_bugs.to_csv(output_file, index=False)

# Example usage:
input_file = 'resolved_issues_cassandra_version3.csv'    # Path to the input Excel file
output_file = 'result_version3.csv'  # Path to the output Excel file

search_algorithm(input_file, output_file)