# getting class attributes in particular order
[foo_class.__dict__[key] for key in my_bar_list if hasattr(foo_class, key)]
