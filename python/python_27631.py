# Start another program and leave it running when the script ends
DETACHED_PROCESS = 0x00000008
pid = subprocess.Popen(["rv", rvFile, '-nc'], creationflags=DETACHED_PROCESS, shell=True).pid
raw_input("= Opened file")
