# Suppose I have this loop in Django...how do I display this?
{% if forloop.counter|divisbleby:"15" %}
    &lt;div class="menu"&gt;abc&lt;/div&gt;
{% endif %}
