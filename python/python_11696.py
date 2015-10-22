# Retrieving an image from mongoengine and display it on a page as http reponse in python
marmot = Animal.objects(genus='Marmota').first()
photo = marmot.photo.read()
content_type = marmot.photo.content_type
