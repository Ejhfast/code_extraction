# use IDs instead of instances to create new objects with foreign keys
a = models.Object1.get_or_create(f__pk=foreign_object_id)
