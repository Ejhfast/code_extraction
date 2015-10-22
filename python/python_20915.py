# make django urls ignore additional params
url(r'^site/(?P&lt;site_level&gt;[^\/]+)/', site_details, name='site_details'),
