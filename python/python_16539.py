# Deadline exceeded while posting multiple cards to timelines with a video attached
urlfetch.set_default_fetch_deadline(45)
httplib2.Http(timeout=45)
