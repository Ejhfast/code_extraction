# In Google App Engine should I not use instance methods in models?
@classmethod
def do_somespecial_query(cls):
    return cls.query().filter(cls.some_property = True)
