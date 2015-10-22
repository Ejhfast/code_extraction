# Is it possible to pass a dictionary with extraneous elements to a Django object.create method?
MyModel.objects.create(**{key: value for key, value in data_dict.iteritems() if key in MyModel._meta.get_all_field_names()})
