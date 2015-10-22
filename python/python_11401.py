# Django multitenant urls configuration
url(r'^[\w\-]+/', include('project.urls_tenant')),
