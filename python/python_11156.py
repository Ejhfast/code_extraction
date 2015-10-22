# Disable static file caching in Tornado
def set_extra_headers(self, path):
    self.set_header("Cache-control", "no-cache")
