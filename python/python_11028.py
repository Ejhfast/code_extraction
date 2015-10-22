# Using variables with a django template
{% with bla=arg|foo %}
  {% url 'view' bla %}
{% endwith %}
