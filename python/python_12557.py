# Get current route instead of route_path in Pyramid
% if request.url == request.route_url('my_route_name')
##do stuff
%endif
