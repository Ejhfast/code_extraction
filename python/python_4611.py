# Low Apache/mod_wsgi throughput
def viewData(request):
    return Response(["aaaaaaaaaa" * 120000])
