# communicate() does not catch suprocess stdout
sub = subprocess.Popen(cmd, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
return sub.communicate()
