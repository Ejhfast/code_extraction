# Multiple modes for line-oriented command interpreters with Python Cmd class
def do_configure(self, line):
    config = ConfigMode(...)
    config.cmdloop()
