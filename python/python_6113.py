# Django: Want to display an empty field as blank rather displaying None
{% if client %} {{client.user}} {% else %} &amp;nbsp; {% endif %}
