# How to use Django translated variable (trans) in template if statement
{% trans "My page Name" as myvar %}
{% if pageName != myvar %}
...
