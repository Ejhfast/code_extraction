# execute 'ls' command as a different User within python script
def my_preexec_fn():
    os.setuid(10033)
process = subprocess.Popen(cmdstr,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, preexec_fn=my_preexec_fn)
