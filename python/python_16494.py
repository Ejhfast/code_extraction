# Add new member to replicas set in mongodb with python and subprocess.call
subprocess.call(["/usr/bin/mongo", "--port", str(port), "--eval", task])
