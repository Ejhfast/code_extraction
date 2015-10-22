# Django Name Groups Urls.py
url(r'^activate/(?P&lt;confirmation_code&gt;[\w]{1,33})/(?P&lt;username&gt;\[\w]+)/$', 'views.activate', {}, 'activate')
