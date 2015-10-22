# Avoid Circular Model Imports in Django Apps
tags = models.ManyToManyField('tags.Tag', ...)
