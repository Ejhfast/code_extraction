# How to inside template check if dictionary's size is larger than 0 and if it is larger that 0 to fetch first key value pair?
{% if some_dict %}
    Some (k, v) - {{ some_dict.items.0 }}
{% endif %}
