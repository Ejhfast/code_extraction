# Django:What is wrong with my code?
class option(models.Model):
    warval =models.ForeignKey(war, null=True)
    value = models.CharField(max_length=10)
