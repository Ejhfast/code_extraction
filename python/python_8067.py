# How to return in-memory PIL image from WSGI application
output = StringIO.StringIO()
base.save(output, format='PNG')
return [output.getvalue()]
