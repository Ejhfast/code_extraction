# Django - How to filter down duplicates in a query?
Books.objects.all().only('title', 'author', 'date').extra(where=['library IS NOT NULL']).distinct()
