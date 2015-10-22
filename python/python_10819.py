# Python: Logging exceptions with custom *kwargs
logger.error('Message with %s', 'args', exc_info=1, extra={...})
