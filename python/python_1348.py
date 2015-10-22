# Mark string as safe in Mako
def __html__(self):
    return unicode(self)
