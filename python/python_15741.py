# Python Google Drive API : uploaded image is shown inside a doc
upload = service.files().insert(
        body=dict(title='test.jpg', mimeType=mime_type),
        media_body=media_body, convert=False).execute()
