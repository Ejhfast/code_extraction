# Django App Dependency Cycle
class MyModel(models.Model):
    myfield = models.ForeignKey('myotherapp.MyOtherModel')
