# How to convert string to list in Django template
{% for image_path in data.image_paths|your_custom_json_decode_filter %}
  {{ image_path }}
{% endfor %}
