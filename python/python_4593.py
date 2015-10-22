# Django - Rebuild a query string without one of the variables
z = request.GET.copy()
del z['a']
