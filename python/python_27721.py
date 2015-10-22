# Listing contents of a bucket with boto3
for object in mybucket.objects.all():
    print(object)
