# Allow colon in Django urls
url(r'^api/(?P&lt;url&gt;[:\/\.\w]+)/$', 'qlu_app.views.api', name='api'),
