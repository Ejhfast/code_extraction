# Configure Django URLS.py to keep #anchors in URL after it rewrites it with a end /
url(r'^(?P&lt;username&gt;[\w-]+)/(?P&lt;cardId&gt;\d+)/?$', 'singleCard.views.singleCard', name='singleCardView'),
