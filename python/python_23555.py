# Can not call dynamically imported python modules
for name in modules:
    getattr(modules[name], name)()
