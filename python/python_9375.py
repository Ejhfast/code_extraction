# Magic-line nav causing some troubles #works only on hrefs included in menu
{% ifequal ourprojects i.menulink|cut:"/" %}current_page_item{% endifequal %}
