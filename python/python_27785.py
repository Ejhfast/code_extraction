# How to edit forms to show fields from second model? And How iterate through manytomany field?
{% for p in shop.product.all %}
{{p.name}}
{% endfor %}
