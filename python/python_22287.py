# python write VLC log file (terminal return) using subprocess.Popen
proc = subprocess.Popen(cmd1, stderr=out, shell=True, preexec_fn=os.setsid)
