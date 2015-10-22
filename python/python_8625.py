# In a Django manager, why use self.get_query_set().get(kwarg=val) rather than self.get(kwarg=val)?
def get(self, *args, **kwargs):
    return self.get_query_set().get(*args, **kwargs)
