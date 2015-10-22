# How to filter for ManyToMany that contains object
boxes = Box.objects.filter(name__startswith='Big', pencils__title='blue')
