# How to get downloadurl of an image in google drive using python?
file = service.files().get(fileId=file_id, fields='downloadUrl').execute()
print file['downloadUrl']
