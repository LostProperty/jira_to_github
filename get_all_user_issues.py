import os
import requests

url = os.getenv('JIRA_URL')
user = os.getenv('JIRA_USER')
password = os.getenv('JIRA_PASSWORD')
user_issues_url = '{0}/rest/api/2/search?jql=assignee={1}'.format(url, user)

r = requests.get(user_issues_url, auth=(user, password))
issues = r.json()['issues']

print('{0} issues'.format(r.json()['total']))
for issue in issues:
    print('{0}: {1}'.format(issue['id'], issue['fields']['summary']))
