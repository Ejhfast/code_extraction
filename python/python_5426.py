# is it possible to Only pull related users through foreign key relationship, once in django
User.objects.exclude(blog=None)
