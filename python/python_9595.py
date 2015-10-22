# Django 1.4 in windows 7 "No FlatPage matches the given query"
url(r'^admin/', include(admin.site.urls)),
url(r'', include('django.contrib.flatpages.urls')), # remove this
