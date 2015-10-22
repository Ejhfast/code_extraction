# Get function parameters as dictionary
def foo(self, arg1, arg2, arg3):
     my_str = "{arg1} went up the {arg2} hill to fetch a pail of {arg3}".
               format(**locals())
