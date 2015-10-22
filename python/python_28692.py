# python's requests do not handle cookies correctly?
self.cookies.update( requests.utils.dict_from_cookiejar(r.cookies) )
