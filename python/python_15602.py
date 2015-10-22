# Redirecting subprocess stdout
task = subprocess.Popen(["python", "test2.py"], stdout=subprocess.PIPE)
print task.communicate()
