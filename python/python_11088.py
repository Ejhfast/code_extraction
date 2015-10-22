# Get number of times an object is referenced in a ManyToManyField
UserProfile.favorite_books.through.objects.filter(book_id=book.id).count()
