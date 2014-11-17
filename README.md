# JIRA to Github

Get issues from JIRA create issues in Github.

## Getting your JIRA issues

You'll need to set the following environment variables. I like to set them in using autoenv
```
export JIRA_USER=your_jira_user
export JIRA_PASSWORD=your_jira_password
export JIRA_URL=jira_url
```

Next run `python get_all_user_issues.py` to see issues assigned to you.

## Posting to Github

You'll need to set the following environment variables
```
export GITHUB_REPO=your_github_repo
export GITHUB_TOKEN=your_github_token
```

`python post_issue_to_github.py {{JIRA_issue_id}}`
