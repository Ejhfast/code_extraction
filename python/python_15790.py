# Django home page URL being rendered as a different URL
urlpatterns = patterns('',
   url(r'', include('app.urls')),
)
