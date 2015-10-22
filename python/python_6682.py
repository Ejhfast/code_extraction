# Popen remote commands
p1 = sp.Popen(["ssh", "user@some_host", "echo \"%s\" | mysql -u ..." % sql], stdout=sp.PIPE)
