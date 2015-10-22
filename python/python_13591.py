# HTTPException: Deadline exceeded while waiting for HTTP response from URL: #deadline
from google.appengine.api import urlfetch
urlfetch.set_default_fetch_deadline(45)
