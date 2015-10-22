# Django - Loading a full image on separate page
{% if  image %}
  &lt;img src="{{ image.url }}" /&gt; &lt;!-- Also note the added quotations... --&gt;
{% endif %}  &lt;!-- This is the line you need to add --&gt;
