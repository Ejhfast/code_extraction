# show parent in child screen django admin python
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description']
