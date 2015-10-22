# How to ensure Blob metadata is kept when copying blob in Python App Engine
file_name = files.blobstore.create(mime_type='image/png',_blobinfo_uploaded_filename=file_name_from_url)
