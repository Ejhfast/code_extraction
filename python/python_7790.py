# Python GAE urlfetch credentials
result = urlfetch.fetch("http://www.domain.com/",
                        headers={"Authorization":
                                 "Basic %s" % base64.b64encode("username:password")})
