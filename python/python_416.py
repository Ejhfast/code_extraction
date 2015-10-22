# How do I detect if my appengine app is being accessed by an iphone/ipod touch?
uastring = self.request.headers.get('user_agent')
if "Mobile" in uastring and "Safari" in uastring:
  # do iphone / ipod stuff
