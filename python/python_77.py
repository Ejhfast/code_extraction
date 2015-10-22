# How do I log an exception at warning- or info-level with trace back using the python logging framework?
logger.warning("something raised an exception: " + excep,exc_info=True)
