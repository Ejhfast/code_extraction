# Django finding static file (1.5) ERROR 404 1649
(r'^static/(?P&lt;path&gt;.*)$', 'django.views.static.serve', {'document_root': '/path/to/your/static/'}),
