# Base64 encode binary uploaded data on the AppEngine
img = Image( name=name, data=file.read() )
img.put()
return ( str(img.name), img.key() )
