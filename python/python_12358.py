# How can I prevent circular {% include %} calls in Jinja2 templates
ast = env.parse(template_text)
    for each in meta.find_referenced_templates(ast) :        # find the (% includes %}
