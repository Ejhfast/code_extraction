# images in django templates
{% for i in arr %}
&lt;img src="{% if i.image %}{{ i.image.url }}{% else %}{{ STATIC IMAGE URL }}{% endif %}" style="width:100px;height:100px;"&gt;
{% endfor %}
