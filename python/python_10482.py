# App Engine : sub folder in templates
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(['templates', 'templates\blog'])
