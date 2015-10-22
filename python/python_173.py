# ForeignKey form restrictions in Django
parents = Category.objects.filter(parent_id=0)
