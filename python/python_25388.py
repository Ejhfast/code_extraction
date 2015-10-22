# Can I use Django's template language to construct HTML for use in a JSON response field?
from django.template.loader import render_to_string
rendered = render_to_string('my_template.html', {'foo': 'bar'})
