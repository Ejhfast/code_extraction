# Python/Django Modeling Question
class TABLE(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('self')
