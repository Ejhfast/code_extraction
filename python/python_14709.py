# Common exception handler for multi-threaded Python application
import signal
signal.signal(signal.SIGINT, signal.SIG_IGN)
