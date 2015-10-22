# javan installation using python script
process = subprocess.Popen(['command plus args as in above link'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = process.communicate()
