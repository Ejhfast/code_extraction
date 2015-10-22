# Pass variables to all Jinja2 templates with Flask
@app.context_processor
def inject_dict_for_all_templates():
    return dict(mydict=code_to_generate_dict())
