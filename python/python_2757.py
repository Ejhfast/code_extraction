# Using Django's memcache API on Dynamically created models
new_class = type(name, (models.Model,), attrs)
mod = sys.modules[new_class.__module__]
mod.__dict__[new_class.__name__] = new_class
