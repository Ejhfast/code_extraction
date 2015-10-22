# configuring urls.py with this regex
(r'^blog/(?P&lt;day&gt;\d{2})-(?P&lt;month&gt;\w{3})-(?P&lt;year&gt;\d{4})/(?P&lt;slug&gt;[-\w]+)/$','blog.views.single_post'),
