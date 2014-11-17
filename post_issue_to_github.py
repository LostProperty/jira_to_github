import sys
import os
import requests
from github import Github


def get_jira_issues_details(issue_id):
    url = os.getenv('JIRA_URL')
    user = os.getenv('JIRA_USER')
    password = os.getenv('JIRA_PASSWORD')
    user_issues_url = '{0}/rest/api/latest/issue/{1}'.format(url, issue_id)
    r = requests.get(user_issues_url, auth=(user, password))
    if r.status_code != 200:
        return False
    return r.json()


def post_to_github(title, description, jira_issue_id):
    repo = os.getenv('GITHUB_REPO')
    token = os.getenv('GITHUB_TOKEN')
    g = Github(token)
    github_repo = g.get_repo(repo)
    # TODO: add client label
    title = 'CLIENT ISSUE: {0}'.format(title)
    description = '{0}\n\nJIRA Issue ID{1}'.format(description, jira_issue_id)
    return github_repo.create_issue(title, description)


jira_issue_id = sys.argv[1]
jira_issue = get_jira_issues_details(jira_issue_id)
title = jira_issue['fields']['summary']
description = jira_issue['fields']['description']
github_issue = post_to_github(title, description, jira_issue_id)
print('Github Issue number: {0}'.format(github_issue.number))
