# How can i change the template for different urls
url(r'^public/search/$', MyView.as_view(template_name="search1.html"), name= 'public_search')
url(r'^private/search/$', MyView.as_view(template_name="search2.html"), name= 'private_search')
