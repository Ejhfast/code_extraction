# How do I get a default Value for a Field that usually increments in Django?
class Bill(models.Model):
    serial = models.IntegerField(default=lambda: Bill.objects.latest('id').serial + 1)
    # ...
