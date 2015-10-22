# Making super() work in Python's urllib2.Request
class ExtendedRequest(urllib2.Request):
    def __init__(self,...):
        urllib2.Request.__init__(self,...)
