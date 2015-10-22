# How can iterate over all the settings in Django?
for s in dir(settings):
    print s, ':', getattr(settings, s)
