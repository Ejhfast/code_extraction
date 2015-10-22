# Serve a dynamically generated image with Django
response = HttpResponse(mimetype="image/png")
img.save(response, "PNG")
return response
