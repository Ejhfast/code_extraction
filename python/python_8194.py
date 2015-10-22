# Django - How do I Iterate through a list of dictionaries to concatenate values from a same element
{%for element in listDict%}
    {{ element.product }} - {{ element.price }}
{% endfor %}
