# Django return specific field from model as foreign key
class Customer(models.Model):
    name = models.CharField(max_length=64)
    myid = models.CharField(primary_key=True, max_length=64)
