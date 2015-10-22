# GAE Python - Saving database query into cookie
self.response.headers.add_header(str('Set-Cookie'), str('shops=%s; path=/; expires=%s') % (shoplist, expire_string))
