# Why can't Pyramid locate this template file?
@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
