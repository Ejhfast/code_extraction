# Cut a string in a Django template that's returned by request.post
{% if request.path|slice:':8' == '/foo/bar' %}...{endif}
