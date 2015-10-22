# Iterating though Dictionary values is not working for me in Django on GAE
{% for data in Data.items %}
     &lt;td&gt;key: {{ data.0 }}: value: {{ data.1 }}&lt;/td&gt;
{% endfor %}
