# How to I disable and re-enable console logging in Python?
logger = logging.getLogger('my-logger')
logger.propagate = False
# now if you use logger it will not log to console.
