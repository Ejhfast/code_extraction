# Can't close processes using selenium threads
proc =  subprocess.Popen( ["python" , path + "/pythonChild.py"], preexec_fn=os.setsid, stdout=subprocess.PIPE ,stdin=subprocess.PIPE)
os.killpg( proc.pid, 9 )
