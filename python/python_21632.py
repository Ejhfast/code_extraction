# Google App Engine: Outputting 'values' from a SearchResult object on Jinja2 template.
{% for result in results %}
  {{ result.fields[0].value }}
{% endfor %}
