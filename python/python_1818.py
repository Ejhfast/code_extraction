# Convert string in base64 to image and save on filesystem in Python
fh = open("imageToSave.png", "wb")
fh.write(imgData.decode('base64'))
fh.close()
