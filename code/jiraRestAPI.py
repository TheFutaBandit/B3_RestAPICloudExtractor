from jira import JIRA
import csv

# Initialize JIRA client
jira = JIRA(server="https://issues.apache.org/jira")

# JQL query with version filter
jql_query = 'project = CASSANDRA AND status = Resolved AND (affectedVersion ~ "3.*" OR fixVersion ~ "3.*") ORDER BY created DESC'

max_results = 1000
total_exported = 0

csv_file_name = 'resolved_issues_cassandra_version3.csv'

with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Bug ID", "Bug Summary", "Bug Description", "Affected Version", "Fix Version"])

    issues = jira.search_issues(jql_query, maxResults=max_results)
    
    for issue in issues:
        bug_id = issue.key
        bug_summary = issue.fields.summary
        bug_description = issue.fields.description

        # Safely get affected versions and fix versions
        affected_versions = getattr(issue.fields, 'versions', [])
        fix_versions = getattr(issue.fields, 'fixVersions', [])

        affected_version_str = ", ".join(v.name for v in affected_versions) if affected_versions else "N/A"
        fix_version_str = ", ".join(v.name for v in fix_versions) if fix_versions else "N/A"

        writer.writerow([bug_id, bug_summary, bug_description, affected_version_str, fix_version_str])
        total_exported += 1

print(f"Data export completed. Total issues exported: {total_exported}")
print(f"Data has been exported to {csv_file_name}")

# Print out the first few rows of the CSV for verification
print("\nFirst few rows of the CSV:")
with open(csv_file_name, mode='r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        if i < 5:  # Print first 5 lines
            print(line.strip())
        else:
            break