# I can't test a Google App using OpenID single sign-on on the AppEngine devserver, locally
def check_email(self, user):
  if os.environ.get('SERVER_SOFTWARE', '').startswith('Dev'):
    return True
