# One-To-Many and Many-To-One relatioships in Django
class Video(models.Model):
    environment = models.ForeignKey(Environment)
