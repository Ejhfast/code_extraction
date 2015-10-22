# Python, AttributeError: RunCmd instance has no attribute 'p' for delta debug
def target():
    self.p = sp.Popen(self.cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)
