# How can I add attributes to a module at run time?
setattr(sys.modules[__name__], 'attr1', 'attr1')
