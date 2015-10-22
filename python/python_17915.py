# Registering a model in Admin page
class SamplemodAdmin(admin.ModelAdmin):
   pass
admin.site.register(Samplemod, SamplemodAdmin)
