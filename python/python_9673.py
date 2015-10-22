# Django Admin modifications for existing extensions (django_taggit)
admin.site.unregister(Tag)
admin.site.register(Tag, YourTagClass)
