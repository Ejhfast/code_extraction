# Python - how to execute shell commands with pipe?
p2 = subprocess.Popen(["grep", "-c", "test"], stdin=p1.stdout, stdout=subprocess.PIPE)
