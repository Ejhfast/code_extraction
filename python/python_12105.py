# flask jinja macros variable in url_for
{% macro icon(site, title="") %}
    &lt;img src="{{ url_for('static', filename='icons/%s.png' % site) }}" alt="{{ title }}" class="img-icon"&gt;
{% endmacro %}
