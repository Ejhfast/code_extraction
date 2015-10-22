# Upload images/video to google cloud storage using Google App Engine
upload_url = blobstore.create_upload_url('/upload_handler', gs_bucket_name='my_bucket')
