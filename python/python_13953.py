# Compare Django template variable with template tag
{% captureas admin_url %}{% url "admin:index" %}{% endcaptureas %}
{% if request.get_full_path == admin_url %}
