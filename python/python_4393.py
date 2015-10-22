# error when running git command inside Popen
subprocess.Popen( '/usr/bin/git status', cwd = os.path.dirname( path ), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
