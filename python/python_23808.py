# Make render call using a URL argument to construct the template file name
return render(request, u'clients/models/%s-%s.json' % (client, report), ...)
