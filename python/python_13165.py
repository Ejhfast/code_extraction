# How can I dynamically create objects in django/python?
types = dict('cat' = CatType, 'dog' = DogType)
newobj = types[type](user = user, cat_id = thing_id)
