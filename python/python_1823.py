# Django - Template not complete rendered
httpresponse_kwargs = {'mimetype': kwargs.pop('mimetype', None)}
return HttpResponse(loader.render_to_string(*args, **kwargs), **httpresponse_kwargs)
