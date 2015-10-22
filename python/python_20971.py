# create background process with Python's Popen
subprocess.Popen(['ping www.google.com &gt; /dev/null &amp;'], shell=True, preexec_fn=os.setsid)
