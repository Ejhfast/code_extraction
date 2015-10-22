# How to extract and then refer to variables defined in a python module?
hosts = [eval('modulename.' + x) for x in dir(local_variables) if '_ip' in x]
