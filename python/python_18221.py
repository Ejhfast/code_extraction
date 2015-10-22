# Is it possible to change jira issue status with python-jira?
if issue.fields.status in ('open', 'reopened'):
    # Move the ticket from opened to closed.
    jira.transition_issue(ticket, transitionId=131)
