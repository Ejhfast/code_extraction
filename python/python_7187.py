# Least painful way to run a Python delay loop
t = threading.Timer(30.0, unban)
t.start() # after 30 seconds, unban will be run
