# store database data into json file using python
path = "{0}/app_name/fixtures/book.json".format(settings.PROJECT_ROOT)
with open(path, "w") as out:
    json_serializer.serialize(Book.objects.all(), stream=out)
