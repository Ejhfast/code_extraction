# Django models: One to one relationship between objects of the same model class
parentFolder = models.ForeignKey('self', unique=False, related_name="childrenFolders")
