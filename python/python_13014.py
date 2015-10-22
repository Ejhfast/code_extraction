# Subprocess: Execute two or more preexec_fn
subprocess.Popen( ..., preexec_fn = lambda : ( os.setegid(1000), os.seteuid(1000)) )
