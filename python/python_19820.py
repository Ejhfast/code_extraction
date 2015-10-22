# Django Group Permission Check in Template
{% if permission in group.permissions.all  %} checked="checked" {% endif %}
