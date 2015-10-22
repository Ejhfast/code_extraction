# Getting names of values passed as *args and **kwargs
def list(self, *args, **kwargs):
    prefix = kwargs.get('prefix', args[0] if args else '')
