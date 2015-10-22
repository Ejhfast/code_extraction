# how to handle white space in filename when using subprocess in python
cmd = "rm 040513\ data.txt"
subprocess.call(cmd, shell=True)
