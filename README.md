Aging-Related Bugs in Cloud Open Source Software (HIVE)

Project Overview
This project studies Aging-Related Bugs (ARBs) in open-source cloud software, specifically Apache HIVE. The main objective is to extract and analyze ARB-prone files to understand the aging effects in cloud software systems.

Process Breakdown
1. Bug Extraction from JIRA
Extracted all bugs for version 3.1.0 of HIVE using the JIRA REST API.
Exported the bugs in CSV format for further analysis.
2. Identifying ARB Prone Bugs
Implemented a search keyword algorithm to scan the bug summaries for ARB-related keywords.
Selected bugs with summaries containing aging-related terms for deeper investigation.
3. Mapping Bug IDs to Source Files
For each identified bug ID, a custom Python script was used to map the bug ID to the respective source files affected by the bug.
This mapping helps in pinpointing which files are prone to aging-related bugs.
Tools and Technologies
JIRA REST API for bug extraction
Python for scripting and file mapping
Keyword search algorithm for filtering relevant bugs

- [ ] Add hadoop-mapreducer
- [ ] Add Storm
- [ ] Add Hive
- [ ] Cassandra
