# Handling application/json data with bottle
def parse(request):
    encoding = ... #get encoding from headers
    return json.load(TextIOWrapper(request.body, encoding=encoding))
