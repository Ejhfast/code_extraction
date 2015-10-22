# HTML templating using Jinja2 No module named your app
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader('%s/templates/' % os.path.dirname(__file__))
)
