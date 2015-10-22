# Jinja2 render context not applied to imported templates
use_macro = ("{% from 'macro' import some_macro with context %}"
             "{{ some_macro() }}")
