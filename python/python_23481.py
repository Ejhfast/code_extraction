# Model, Performing an OR and a ordered by
Product.objects.filter(Q(categoryproduct__category=self) | Q(categoryproduct__category__category=self), active=True)
