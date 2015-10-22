# Filtering on multiple values from a single field - Django
mylist = AboutMe.objects.all().filter(MyG__in=mygpref)
