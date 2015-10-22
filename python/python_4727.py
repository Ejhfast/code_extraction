# How do I stream a file using werkzeug?
g = file(path_to_bigfile) # or any generator
return Response(g, direct_passthrough=True)
