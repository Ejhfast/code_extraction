# Tornado template loader from string - Heroku
from tornado.template import Template
t = Template(my_template_string_from_database)
r = t.generate(key=value) #as we do in loader
