# A 'related content' list with DetailView in Django
Article.objects.filter(category__in=self.object.categories.all())
