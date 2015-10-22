# Django 1.8.3: Showing many-to-many additional fields in template
{% for rolling in project_info.role_set.all %}
        {{rolling}}
    {% endfor %}
