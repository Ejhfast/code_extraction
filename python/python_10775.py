# Resize an image retrieved from Google Drive using API
theGoogleDriveFile = service.files().get(fileId=&lt;googleDriveFileId&gt;).execute()
result = urlfetch.fetch(theGoogleDriveFile['webContentLink'])
resizedImage = images.resize(result.content, 32, 32)
