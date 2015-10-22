# python equivalent for curl --interface
class BindableHTTPHandler(urllib2.HTTPHandler):
    def http_open(self, req):
        return self.do_open(BindableHTTPConnectionFactory('10.91.56.4'), req)
