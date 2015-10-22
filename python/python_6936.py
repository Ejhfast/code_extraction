# How do I make a query where it filters everything that starts with a number in Django?
Book.objects.filter(title__regex=r'\d')
