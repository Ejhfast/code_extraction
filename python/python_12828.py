# How to clear/reset all configured logging handlers in Python?
print logging.Logger.manager.loggerDict.keys()
