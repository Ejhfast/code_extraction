# How to use Popen to run backgroud process and avoid zombie?
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
