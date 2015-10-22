# Prevent error in Django template when getting width of an ImageField missing an image
{% if myobject.image %}
    {{ myobject.image.width }}
{% endif %}
