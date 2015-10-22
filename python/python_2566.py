# python - Which is the better way to enable/disable logging?
if logger.isEnabledFor(logging.DEBUG):
    logger.debug("Message with %s, %s", expensive_func1(),
                                        expensive_func2())
