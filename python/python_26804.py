# Python: How can the origin IP of an http request be determined
req_ip = request.remote_addr
return Response(req_ip)
