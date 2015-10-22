# Regex + Python - Converting multiple commands into one or fewer commands
variable = re.search("[a-zA-Z0-9]+[a-zA-Z0-9\-' ]+[a-zA-Z0-9]+", variable).group(0)
variable = re.sub("([ '\-])\\1+", "\\1", variable)
