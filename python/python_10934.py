# MongoEngine map_reduce merge collections
for i in FOO.objects.map_reduce(map_f, reduce_f, {"merge":"COLLECTION_NAME"}):
    pass
