# How SIGINT gets passed to grandchild (and how to do this programmatically)
os.kill(-os.getpgid(os.getpid()),signal.SIGINT)
