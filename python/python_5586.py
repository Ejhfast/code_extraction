# from <module> import ... in __init__.py makes module name visible?
setattr(sys.modules["P"], "S", sys.modules["P.S"])
