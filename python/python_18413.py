# How to return default value if field is NULL?
MyModel.objects.extra(select={'field': "coalesce(field, 'Empty')"})
