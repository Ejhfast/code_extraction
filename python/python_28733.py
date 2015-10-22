# Random on model fields generates infinite migration
class Shop(models.Model):
    ...
    code = models.CharField(max_length=4, default=generate_random_code)
