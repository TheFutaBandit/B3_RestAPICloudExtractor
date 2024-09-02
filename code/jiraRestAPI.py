from jira import JIRA
import csv

jira = JIRA(server="https://issues.apache.org/jira")

jql_query = 'project = CASSANDRA AND status = Resolved'

start_at = 0
max_results = 10

issues = jira.search_issues(jql_query, startAt=start_at, maxResults=max_results)

csv_file_name = 'resolved_issues_cassandra.csv'

with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(["Bug ID", "Bug Summary", "Bug Description"])
    
    for issue in issues:
        bug_id = issue.key
        bug_summary = issue.fields.summary
        bug_description = issue.fields.description
        
        writer.writerow([bug_id, bug_summary, bug_description])
print(f"Data has been exported to {csv_file_name}")
