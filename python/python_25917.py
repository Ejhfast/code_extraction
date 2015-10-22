# find a set of path within a string using regex in python
artifact_paths = re.findall(r"^Deploying artifact: .*$", full_string, re.M)
