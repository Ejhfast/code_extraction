# Retrieving netstat from local server python script
subprocess.Popen(['ssh','server','netstat','-a'],stdout=file1)
