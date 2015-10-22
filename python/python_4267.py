# How to add commas / delimiters for all list items except last?
{% for u in users %}
{{u.name}}{% if not forloop.last %},{% endif %}
{% endfor }
