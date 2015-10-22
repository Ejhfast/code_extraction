# HTTPConnection timeout not kickin in as expected
def wakeup():
    subprocess.Popen(["/bin/ping", "-c2", "-w"+str(WAKETIME), PINGHOST], stdout=subprocess.PIPE).stdout.read()
