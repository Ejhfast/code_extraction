# Git add through python subprocess
subprocess.Popen([gitPath] + dirList + ['add','.'], cwd='/home/me/workdir')
