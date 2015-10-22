# bootstrap data-source issue w flask/wtform
{% with autoc_json = autoc|tojson|safe %}
     {{form.name(**{"data-provide":"typeahead","data-source": autoc_json })}}
{% endwith %}
