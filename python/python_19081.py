# How do you unit test a file post with webapp2?
post_contents = {'someVar':file_contents}
request = webapp2.Request.blank('/', POST=post_contents)
response = request.get_response(main.app)
