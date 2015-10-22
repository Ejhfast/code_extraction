# Amazon S3 boto - how to delete folder?
for key in bucket.list(prefix='/your/directory/'):
    key.delete()
