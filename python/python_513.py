# python instance variables as optional arguments
def foo(self, blah=None):
    if blah is None: # faster than blah == None - thanks to kcwu
        blah = self.instance_var
