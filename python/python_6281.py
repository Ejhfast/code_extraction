# Print all properties of an App Engine Model
@register.filter
def mygetattr(obj, name):
    return getattr(obj, name)
