# How to avoid writing request.GET.get() twice in order to print it?
q = request.GET.get('q')
if q:
    print q
