# How to determine if an HTTP request is asynchronous in Python or Pylons
def isAjax(request):
    return request.environ.get('HTTP_X_REQUEST_WITH') == 'XMLHttpRequest'
