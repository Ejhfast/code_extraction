# How to to read a jinja context variable
result = template.render({'a' : "value-1" })
# in the template {% set b = "value-2" %}
b = template.module.b
