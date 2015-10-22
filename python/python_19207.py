# Not able to parse output of bash from Python correctly
subprocess.Popen(["bash", "-c", "make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
