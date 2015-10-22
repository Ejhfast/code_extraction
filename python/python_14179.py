# Why does Popen.communicate() return b'hi\n' instead of 'hi'?
print(subprocess.Popen("echo -n hi", \
    shell=True, stdout=subprocess.PIPE).communicate()[0])
