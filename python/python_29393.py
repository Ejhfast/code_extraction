# flask-wtform placeholder behavior
{% macro form_field(field) %}
{{ field(placeholder=field.label.text) }}
{% endmacro %}
