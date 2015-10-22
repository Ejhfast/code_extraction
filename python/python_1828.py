# Why am I getting this error in Django (I'm trying to do a 304 not modified)
def list_ajax_etag(request):
    return str(request.GET.get('l',''))+str(request.GET.get('a',''))
