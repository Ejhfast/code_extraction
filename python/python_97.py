# Django: Overriding verbose_name for AutoField without dropping the model
class Entry(models.Model):
   id = models.AutoField(verbose_name="custom name")
   # and other fields...
