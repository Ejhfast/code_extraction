# Accessing a specific dictionary inside a dictionary - Django Templates
{% for key, item in myDict.items %}
    {% for innerkey, inneritem in item.items %}
        ...
