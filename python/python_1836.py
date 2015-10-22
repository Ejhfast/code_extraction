# Remove default apps from Django-admin
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
