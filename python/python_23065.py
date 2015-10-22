# How to check in Django if the date was yesterday
{% if accounts.date &lt; today %}
   {{ accounts.name }}
{% endif %}
