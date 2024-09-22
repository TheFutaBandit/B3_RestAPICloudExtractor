import requests
import csv

# GitHub API Configuration
GITHUB_TOKEN = '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'
REPO_OWNER = 'apache'
REPO_NAME = 'storm'
BRANCH_NAME = '2.3.x-branch'  # Branch name for the API request
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}'

# Headers for GitHub API requests
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def fetch_file_content(filepath):
    """Fetch the content of a file from the GitHub repository."""
    url = f'{GITHUB_API_URL}/contents/{filepath}?ref={BRANCH_NAME}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.json().get('content', '')
        return content
    else:
        return None

def is_public_class_file(content):
    """Check if the file content contains a public class."""
    import base64
    decoded_content = base64.b64decode(content).decode('utf-8', errors='ignore')
    return 'public class' in decoded_content

def process_csv(input_csv, output_csv, batch_size=50):
    """Process the input CSV in batches to check for public class files and export results."""
    results = []
    public_class_count = 0

    def process_batch(batch):
        nonlocal public_class_count
        for file_path in batch:
            if file_path.startswith('/'):
                file_path = file_path[1:]

            content = fetch_file_content(file_path)
            if content is not None:
                if is_public_class_file(content):
                    results.append({'File': file_path, 'Is_Public_Class': 'Yes'})
                    public_class_count += 1
                else:
                    results.append({'File': file_path, 'Is_Public_Class': 'No'})
            else:
                results.append({'File': file_path, 'Is_Public_Class': 'File Not Found'})

    # Read the input CSV file
    with open(input_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        batch = []
        for row in reader:
            batch.append(row['File'])
            if len(batch) >= batch_size:
                process_batch(batch)
                batch = []

        if batch:
            process_batch(batch)

    # Write the results to the output CSV file
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['File', 'Is_Public_Class'])
        writer.writeheader()
        writer.writerows(results)

    # Print the number of public class files
    print(f"Number of public class files: {public_class_count}")

def main():
    input_csv = 'dataset/STORM_ExistingFiles_JavaFilter.csv'  # Input CSV file with file paths
    output_csv = 'dataset/STORM_PublicClassFiles.csv'  # Output CSV file with public class check results
    process_csv(input_csv, output_csv)
    print(f"Processed CSV file and exported results to {output_csv}")

if __name__ == "__main__":
    main()
