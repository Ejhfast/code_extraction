# Django: Saving an image file from a form
im = Image.open(StringIO(request.FILES['im'].read()))
