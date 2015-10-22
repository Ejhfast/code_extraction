# django delete self and not a self referential entity
user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
