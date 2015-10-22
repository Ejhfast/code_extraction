# Django, a problem about zip file response
response = HttpResponse(open(file_path, 'rb').read(),\
                             content_type='application/zip')
