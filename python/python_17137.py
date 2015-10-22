# jinja: Escape variable + concatenate
{% set escaped =  "&lt;div&gt;&lt;/div&gt;"|e %}
{{ '&lt;div&gt;'|safe + escaped + '&lt;/div&gt;'|safe  }}
