# Django ORM way of going through multiple Many-to-Many relationship
Toy.objects.filter(toy_owners__parents=parent)
