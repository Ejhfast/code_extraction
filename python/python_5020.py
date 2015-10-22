# How do you sort a list in Jinja2?
{% for movie in movie_list|sort(attribute='rating') %}
