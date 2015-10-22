# add POST HOOK to a bitbucket repository using their REST API and python-requests
requests.post(request_url, auth=(repo_user, repo_pass), data='type=POST&amp;URL=hooks.url.com')
