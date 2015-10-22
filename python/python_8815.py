# App Engine Python: How to properly redirect to a template
import urllib
self.redirect("sites.htm?%s" % urllib.urlencode(dict(a="this and that", b="back and forth)))
