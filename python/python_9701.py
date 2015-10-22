# Twisted http server with async response where requests have to wait for data to become available or timeout
def ret(self, result, request):
    request.write(result)
    request.finish()
