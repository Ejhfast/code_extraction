# django reverse URL not matching
url(r'^save/(?P&lt;when&gt;\d{4}-\d{2}-\d{2})/(?P&lt;from_city&gt;[a-zA-Z ]+)/(?P&lt;to_city&gt;[a-zA-Z ]+)/',
  kernel.views.TripSaveView.as_view(),
  name='trip/save'),
