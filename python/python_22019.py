# Django: How to set a (permanent) cookie, in addition to temp session, in Class based views?
response = render(request, template, context)
response.set_cookie('my_cookie', 'my_cookie_value')
return response
