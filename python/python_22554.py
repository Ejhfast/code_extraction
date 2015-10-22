# Python: "import JSON... json.loads(request.body)" 2.7->3.4
# Let's just assume the request is UTF-8 encoded.
data = json.loads(request.body.decode('utf-8'))
