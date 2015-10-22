# Django Templates display list
{% for author in authors %}
    &lt;li&gt;{{ author|safe }}&lt;/li&gt;
{% endfor %}
