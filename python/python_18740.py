# how to have unicode characters in django url?
url(r'^phrase/(?P&lt;lang&gt;[_A-Za-z]+)/(?P&lt;phrase&gt;([^/]+))/$', 'gs.langdb.views.phrases'),
