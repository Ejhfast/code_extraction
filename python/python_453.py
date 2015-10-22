# How to get publisher.authors when you have book.publisher and book.author?
publisher = Publisher.objects.get(...)
authors = Author.objects.filter(book__publisher=publisher).distinct()
