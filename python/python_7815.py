# Regular expression not working in django
url(r'^fieldguide/(?P&lt;IDmatch&gt;0[eE]([0-9A-Fa-f]{0,14}))/$', 'treeView', name='index'),
url(r'^fieldguide/.*$', 'treeDirect', name='index-redirect'),
