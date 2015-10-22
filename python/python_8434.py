# Add metadata to image upload to S3 with Python
k.set_metadata('Content-Type', mime)
k.set_contents_from_file(data, policy='public-read')
k.set_acl('public-read')
