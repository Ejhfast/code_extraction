# How to send header in flask send_file?
response = make_response(send_file(mp3_filepath))
response.headers['X-Something'] = 'header value goes here'
return response
