# How can I use multiple variables(paramaters) in a url in django
url(r'^production/(?P&lt;filler&gt;\w{7})/(?P&lt;day&gt;.*)/$', views.CasesByDay.as_view()),
