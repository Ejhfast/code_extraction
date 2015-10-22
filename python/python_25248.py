# Get Binary Representation of PIL Image Without Saving
s = StringIO.StringIO()
window.save(s, "jpg")
encodedWindow = base64.b64encode(s.getvalue())
