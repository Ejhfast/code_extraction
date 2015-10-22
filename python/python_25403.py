# Show replies to individual comments in Django
{% for Reply in Comment.reply_set.all %}
    {{ Reply.body }}
{% endfor %}
