# Adding dynamic string to logger format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s {0}'.format(var))
