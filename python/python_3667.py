# Django Admin - Disable the 'Add' action for a specific model
class MyAdmin(admin.ModelAdmin):
     def has_add_permission(self, request):
        return False
