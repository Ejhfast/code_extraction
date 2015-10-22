# Different page for logged in vs not logged in user on server vs javascript
{% if user.is_authenticated %}{% block form %}
{% else %} something else {% endif %}
