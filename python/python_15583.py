# Reverse Relation Search Django Admin Interface
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('tags__title',)
