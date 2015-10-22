# Pyramid - How do I create a route that avoids authentication
@view_config(route_name='home', permission=pyramid.security.NO_PERMISSION_REQUIRED)
def open_view(request):
    # ...
