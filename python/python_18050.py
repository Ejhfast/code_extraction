# Django - How to group data from different models into one set of data?
{% for s in Tecs %}
{{ s.auteur }} &lt;-----&gt; {{ s.enterprise.ville }}
{% endfor %}
