# Terminate all subprocesses if any one of subprocess has error
for proc in procs:
    if proc.poll() is not None:  # it has terminated
        # check returncode and handle success / failure
