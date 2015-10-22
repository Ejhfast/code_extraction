# How do I use the the Django ORM to query this many-to-many example?
books = Book.objects.filter(authorbook__author_id=1)
