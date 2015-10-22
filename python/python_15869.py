# how to establish in models file that a django model should be defined as NOT NULL?
class sth(models.Model):
    somefield = models.CharField(max_length = 20, null = False, blank = False)
