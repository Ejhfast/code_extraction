# How to read images from directory, assemble them in <img src="">, and have flask return image?
{% for image in images %}
&lt;img src="{{url_for('static', filename='image/')}}{{image}}"&gt;&lt;/img&gt;
{% endfor %}
