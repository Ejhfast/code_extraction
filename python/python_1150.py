# What may be the problem (Django views)...?
def mainpage(request):
    f=open('gui/pages/index.html','r').readlines()
    return HttpResponse(f)
