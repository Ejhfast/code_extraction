# BytesIO stream image is blank when uploading SimpleUploadedFile
avatar = Avatar.generate(128, self.display_name, "JPEG")
avatar.seek(0) # &lt;---
self.avatar = SimpleUploadedFile("temp.jpeg", avatar.read())
