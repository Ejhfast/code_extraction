# Python: Get a list of changed files between two commits or branches
subprocess.check_output(['git', 'diff', '--name-only', currentBranch + '..' + compBranch])
