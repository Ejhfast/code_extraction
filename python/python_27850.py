# render jinja2 template without a Flask context
with app.app_context():
    data = render_template(path, **context)
