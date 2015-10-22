# Python Requests and 404 error with Django/tasty-pie
request_params = { 'name_regex' : '', 'format' : 'json' }
r = requests.get( 'http://localhost:8000/api/v1/host/', params = request_params )
