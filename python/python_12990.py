# Viewing and filtering models: admin panel or not admin panel?
urlpatterns = patterns('',
    (r'^', include(admin.site.urls)),
)
