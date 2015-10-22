# Implementing "Starts with" and "Ends with" queries with Google App Engine
MyModel.all().filter('prop &gt;=', prefix).filter('prop &lt;', prefix + u'\ufffd')
