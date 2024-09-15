import requests


GITHUB_TOKEN = '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'  
REPO_OWNER = 'apache'
REPO_NAME = 'cassandra'
JIRA_BUG_ID = 'CASSANDRA-19880' 


GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}'


headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def search_commits_for_bug_id(bug_id):
    search_url = f"https://api.github.com/search/commits?q={bug_id}+repo:{REPO_OWNER}/{REPO_NAME}"
    print(f"Searching for commits with URL: {search_url}")
    response = requests.get(search_url, headers=headers)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 401:
        print("Authentication failed. Check your GitHub token.")
    response.raise_for_status()
    results = response.json()
    
    if 'items' in results and len(results['items']) > 0:
        # Collect all commit SHAs
        commit_shas = [item['sha'] for item in results['items']]
        return commit_shas
    else:
        print(f"No commits found for bug ID: {bug_id}")
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

def main():
    # Step 1: Search for the commits associated with the JIRA bug ID
    commit_shas = search_commits_for_bug_id(JIRA_BUG_ID)
    
    if commit_shas:
        print(f"Found {len(commit_shas)} commits for bug ID: {JIRA_BUG_ID}")
        
        # Step 2: Get the files changed in each commit
        for commit_sha in commit_shas:
            print(f"\nCommit SHA: {commit_sha}")
            files_changed = get_files_changed_in_commit(commit_sha)
            
            print("Files changed in the commit:")
            for file in files_changed:
                print(file)
    else:
        print(f"No commits found for JIRA bug ID: {JIRA_BUG_ID}")


if __name__ == "__main__":
    main()
