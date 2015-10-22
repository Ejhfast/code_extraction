# Making a Foreign Key to an option of two different classes in Django
content_type = models.ForeignKey(ContentType)
object_id = models.PositiveIntegerField()
content_object = generic.GenericForeignKey('content_type', 'object_id')
