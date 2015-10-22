# Using app engine interactive console with jinja2 template
from jinja2 import Template
template = Template('Hello {{ name }}!')
print template.render(name='John Doe')
