# Pass binary data to os.system call
pipe = os.popen("something.exe -", "w")
pipe.write(bin)
pipe.close()
