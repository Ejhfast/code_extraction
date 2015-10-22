# How to make Twisted use Python logging?
from twisted.python import log
observer = log.PythonLoggingObserver(loggerName='logname')
observer.start()
