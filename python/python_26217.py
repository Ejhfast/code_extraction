# How to create a new repository with PyGithub
g = Github(token)
user = g.get_user()
repo = user.create_repo(full_name)
