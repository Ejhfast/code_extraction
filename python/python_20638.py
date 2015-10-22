# Can't read from NamedTemporaryFile after being written
file.seek(0)
logging.debug(file.readlines())
