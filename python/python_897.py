# Optional get parameters in django?
url(r'^so/(?P&lt;required&gt;\d+)/$', 'myapp.so', name='something'),
url(r'^so/(?P&lt;required&gt;\d+)/(?P&lt;optional&gt;.*)/$', 'myapp.so', name='something_else'),
