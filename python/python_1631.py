# Reduce strings in python to a specific point
newString = oldString[:oldString[:-1].rfind('/')]
 # strip out trailing slash    ----^       ^---- find last remaining slash
