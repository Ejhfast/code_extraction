# Get form data using python
form = cgi.FieldStorage()
name = form['name'].value
print 'Hello ' + name
