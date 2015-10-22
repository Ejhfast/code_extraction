# App Engine - Specify entity name at runtime
def get_my_class(name):
    return type(name, (db.Expando,), {})
