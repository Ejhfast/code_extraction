# Django programming error 1146 table doesn't exist
tag_choices = ((obj.id, obj.tag) for obj in BlogTag.objects.all())
