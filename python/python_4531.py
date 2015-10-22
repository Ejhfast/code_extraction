# Django: use render_to_response and set cookie
response = render_to_response(template_name, locals(), context-etc..)
response.set_cookie("favorite_color",request.GET["favorite_color"])
return response
