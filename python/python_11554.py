# How to clear the log file and write it again?
MAX_SIZE = 300 * 1024 * 1024
LOG_PATH = fdoc_log + "/plus_dig_cname.log"
fh = logging.handlers.RotatingFileHandler(LOG_PATH, maxBytes=MAX_SIZE, backupCount=5)
