# How can I pull a remote repository with GitPython?
repo = git.Repo('repo_name')
 o = repo.remotes.origin
 o.pull()
