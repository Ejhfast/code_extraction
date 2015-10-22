# Combining abstract model class and multi-table inheritance in Django
class Profile(BaseProfile):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    ...
