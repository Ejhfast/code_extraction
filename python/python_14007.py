# Editing django-rest-framework serializer object before save
if serializer.is_valid():
    serializer.object.user_id = 15 # &lt;----- this line
    serializer.save()
