# check output from CalledProcessError
output = subprocess.check_output(["ping", "-c","2", "-W","2", "1.1.1.1"])
