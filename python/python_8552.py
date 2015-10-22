# Image upload: iPhone Client - Django - S3
for file_chunk in uploaded_file.chunks():
    saved_file.write(file_chunk)
