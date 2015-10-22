# ValidationError from mandrill with google app engine's urlfetch
import json
content = urlfetch.fetch(mandrill_url, method=urlfetch.POST, headers={'Content-Type': 'application/json'}, payload=json.dumps(my_payload))
