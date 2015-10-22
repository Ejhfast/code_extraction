# Django 1.4 - Redirect to Non-HTTP urls
response = HttpResponse("", status=302)
response['Location'] = "appdev://..."
return response
