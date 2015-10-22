# Script to Mobile-Friendly test
get the inbuilt function's method name which is passed as an argument and call inside function body
def logging_template(logger_name, level, message):
    logger = logging.getLogger(logger_name)
    getattr(logger, level)(message)
