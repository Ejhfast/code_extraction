# Get Root URL/Domain Name in Email Template
&gt;&gt;&gt; from django.contrib.sites.models import Site
&gt;&gt;&gt; Site.objects.get_current().domain
"example.com"
