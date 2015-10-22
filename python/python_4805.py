# Cant seem to find how to check for valid emails in App Engine
from google.appengine.api import mail
if not mail.is_email_valid(to_addr):
  # Return an error message...
