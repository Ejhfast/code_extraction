# Boto s3 get_metadata
for key in bucket.list():
   akey = bucket.get_key(key.name)
   print akey.get_metadata("company")
