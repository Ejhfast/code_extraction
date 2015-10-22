# Passing an attribute from method to another method python
def gather_path(self):
    path_object = PathsOfDomain.objects.filter(FKtoTld=3)
