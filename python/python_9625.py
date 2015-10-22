# s3- boto- list files within a bucket by upload time
orderedList = sorted(bucketList, key=lambda k: k.last_modified)
keysYouWant = orderedList[0:100]
