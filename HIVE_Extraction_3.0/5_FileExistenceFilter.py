import pandas as pd
import requests
import csv
import sys

# Increase CSV field size limit to handle larger fields
csv.field_size_limit(sys.maxsize)

# GitHub API Configuration
GITHUB_TOKEN = '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'
REPO_OWNER = 'apache'
REPO_NAME = 'hive'
BRANCH_NAME = 'branch-3.1'  # Branch name for the API request
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}'

# Headers for GitHub API requests
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def file_exists_in_github(filepath):
    """Check if a file exists in the GitHub repository."""
    url = f'{GITHUB_API_URL}/contents/{filepath}?ref={BRANCH_NAME}'
    response = requests.get(url, headers=headers)
    return response.status_code == 200

def process_csv(input_csv, output_csv):
    """Process the input CSV to filter files and export results to a new CSV."""
    results = []
    
    # Read the input CSV file
    with open(input_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            file_path = row['File']
            # Ensure the file path is correctly formatted (remove leading slashes if any)
            if file_path.startswith('/'):
                file_path = file_path[1:]
            
            # Check if the file exists in the GitHub repository
            if file_exists_in_github(file_path):
                results.append(row)
            else:
                print(f"File not found in GitHub: {file_path}")
    
    # Write the results to the output CSV file
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Bug_ID', 'File'])
        writer.writeheader()
        writer.writerows(results)

def main():
    input_csv = 'dataset/HIVE_ARBFiles_JavaFilter_Grouped.csv'  # Input CSV file containing the 'File' column
    output_csv = 'dataset/HIVE_ExistingFiles_JavaFilter.csv'  # Output CSV file to store the results
    process_csv(input_csv, output_csv)
    print(f"Processed CSV file and exported results to {output_csv}")

if __name__ == "__main__":
    main()
