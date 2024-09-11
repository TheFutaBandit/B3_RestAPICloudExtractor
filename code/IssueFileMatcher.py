import requests
import re

# Example: Query GitHub API for commit details
def get_commit_files(commit_hash):
    url = f"https://api.github.com/repos/apache/cassandra/commits/c53d3ac8c6a743b7e730d2ac358516842b024133"
    response = requests.get(url)
    data = response.json()
    
    files = data.get('files', [])
    return files

# Example: Parse the diff and find relevant files based on keywords from Jira
def find_relevant_files(commit_hash, bug_summary):
    files = get_commit_files(commit_hash)
    
    # Extract keywords from the bug summary
    keywords = re.findall(r'\w+', bug_summary.lower())
    
    relevant_files = []
    
    for file in files:
        # Check the diff content for matches
        diff = file.get('patch', '').lower()
        if any(keyword in diff for keyword in keywords):
            relevant_files.append(file['filename'])
    
    return relevant_files

# Example usage
commit_hash = "c53d3ac8c6a743b7e730d2ac358516842b024133"  # Replace with actual commit hash
bug_summary = "With enableTracing set to true, the unset() method of a BoundStatement for a map type field failed during execution"
relevant_files = find_relevant_files(commit_hash, bug_summary)

print(f"Relevant files for bug: {relevant_files}")