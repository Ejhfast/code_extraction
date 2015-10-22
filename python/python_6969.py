# small problem with django-tinymce and django-filebrowser integration
fb_url = "%s://%s%s" % (request.is_secure() and 'https' or 'http',
    #request.get_host(), urlresolvers.reverse('filebrowser-index'))
    request.get_host(), urlresolvers.reverse('fb_browse'))
