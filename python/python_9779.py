# Pyramid: Views registered with `view_config` not being associated with routes
@view_config(route_name='hello')
def hello(request):
    return Response("Hello, world!")
