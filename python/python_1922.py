# Filter across three tables using Django
LitAgent.objects.filter(author__book__year_published=2006)
