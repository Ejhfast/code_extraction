# python: unintentionally modifying parameters passed into a function
self.fields = dict( key, value for key, value in fields.items()
                     if accept_key(key, data) )
