import requests
import csv
import sys
import time  # Import time module for adding delays

# Increase CSV field size limit to handle larger fields
csv.field_size_limit(sys.maxsize)

# GitHub API Configuration
GITHUB_TOKEN = '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'
REPO_OWNER = 'apache'
REPO_NAME = 'hive'
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}'

# Headers for GitHub API requests
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def search_commits_for_bug_id(bug_id):
    """Search commits for a specific bug ID."""
    search_url = f"https://api.github.com/search/commits?q={bug_id}+repo:{REPO_OWNER}/{REPO_NAME}"
    response = requests.get(search_url, headers=headers)
    if response.status_code == 401:
        print("Authentication failed. Check your GitHub token.")
        return None
    elif response.status_code == 403:
        print("Rate limit exceeded. Waiting for a while before retrying...")
        time.sleep(60)  # Wait for 60 seconds before retrying
        return search_commits_for_bug_id(bug_id)  # Retry the request
    response.raise_for_status()
    results = response.json()
    
    if 'items' in results and len(results['items']) > 0:
        commit_shas = [item['sha'] for item in results['items']]
        return commit_shas
    else:
        return None

def get_files_changed_in_commit(commit_sha):
    """Get the files changed in a specific commit."""
    commit_url = f"{GITHUB_API_URL}/commits/{commit_sha}"
    response = requests.get(commit_url, headers=headers)
    response.raise_for_status()
    commit_data = response.json()
    
    # Extracting the filenames from the commit data
    files_changed = [file['filename'] for file in commit_data.get('files', [])]
    return files_changed

def process_csv(input_csv, output_csv):
    """Process the input CSV to find files associated with each bug ID and export results to a new CSV."""
    results = []
    
    # Read the input CSV file
    with open(input_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            bug_id = row['Bug_ID']
            commit_shas = search_commits_for_bug_id(bug_id)
            
            if commit_shas:
                for commit_sha in commit_shas:
                    files_changed = get_files_changed_in_commit(commit_sha)
                    for file in files_changed:
                        results.append({'Bug_ID': bug_id, 'File': file})
            else:
                print(f"No commits found for Bug ID: {bug_id}")
            
            # Add a delay between requests to avoid rate limiting
            time.sleep(2)  # Wait for 2 seconds between requests
    
    # Write the results to the output CSV file
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Bug_ID', 'File'])
        writer.writeheader()
        writer.writerows(results)

def main():
    input_csv = 'dataset/HIVE_ARBIssues_3.csv'  # Input CSV file containing the 'Bug ID' column
    output_csv = 'dataset/HIVE_ARBFiles_3.csv'  # Output CSV file to store the results
    process_csv(input_csv, output_csv)
    print(f"Processed CSV file and exported results to {output_csv} ")

if __name__ == "__main__":
    main()
