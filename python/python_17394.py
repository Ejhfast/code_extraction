# How to order a set of object in a view
{% for domain in server.domain_set.all|dictsort:'url' %}
