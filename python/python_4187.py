# Internationalization of models in Django applications
class XType(models.Model):
    language = models.CharField(max_length=5)
    description = models.CharField(max_length=50)
