# Post image to facebook via python and graphapi
self.client = GraphAPI(ACCESS_TOKEN)
with open("test.jpg","rb") as image:
    self.client.put_photo(image, "test post from app - please ignore")
