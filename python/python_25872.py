# Using middleware to add arguments to view functions in django
def APIMiddleware(object):
    def process_request(self, request):
        request.api = API(host, port, user, password, extra={"url": request.get_full_path()})
