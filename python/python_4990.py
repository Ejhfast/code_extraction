# how to switch into a single database among multiple databases at run time in django?
Author.objects.using('db_name').all()
