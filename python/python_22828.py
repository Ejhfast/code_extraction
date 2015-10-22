# Django - urls.py in project, and url.py in app
urlpatterns = patterns('StripCal.views',
url(r'^$', 'index', name='index'),
url(r'^run','detail', name='detail'),
