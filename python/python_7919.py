# Getting ValueError as response to http request in Django framework
def proj_view(request, cust):
    return HttpResponse("project overview for cust: %s." % cust)
