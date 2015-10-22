# How to save site on Django from sql injections with slug
url(r'^blog/(?P&lt;slug&gt;[\w-]+)/$', PostDetail.as_view(), name='post'),
