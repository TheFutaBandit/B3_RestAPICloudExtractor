from jira import JIRA
import csv

jira = JIRA(server="https://issues.apache.org/jira")

counter = 0

issues = jira.search_issues("project = HIVE and fixVersion = '3.1.0'", maxResults=1000)
    
csv_file_name = "dataset/HIVE_Closed_3.csv"

with open(csv_file_name, mode = 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(["Bug_ID", "Bug_Summary", "Bug_Description"])

    for issue in issues:
        bug_id = issue.key
        bug_summary = issue.fields.summary
        bug_description = issue.fields.description
        counter += 1
        writer.writerow([bug_id,bug_summary,bug_description])

print(f"data export successful with {counter} results")


