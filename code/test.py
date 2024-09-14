import requests

# GitHub API Configuration
GITHUB_TOKEN = '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'
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Check rate limit status
response = requests.get('https://api.github.com/rate_limit', headers=headers)
print(response.json())
