# Store the output of Subprocess.call in a String
x=subprocess.Popen("grep 'xyz-pqr' textfile_5906.txt",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=x.communicate()
