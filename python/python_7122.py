#  Django:How to let 3rd party sites access images on your server.(limited access i.e. only to that folder)
def test(request,name): name = str(name)+".jpg" url = "Users/admin/workspace/bolt/templates/media/images/photos/" full =url+name image_data = open(full, "rb").read() return HttpResponse(image_data, mimetype="image/png")
