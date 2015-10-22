# How to iterate over arguments
for arg in vars(args):
     print arg, getattr(args, arg)
