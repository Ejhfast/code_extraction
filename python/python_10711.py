# Tastypie, filtering many to many relationships
tags = fields.ToManyField('django_app.api.TagsResource', attribute=lambda bundle: bundle.obj.tags.filter(tags__deleted=0))
