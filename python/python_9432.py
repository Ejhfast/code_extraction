# Django-cms haystack search - placeholder content
{{ result.object.get_title }}
{% highlight result.text with request.GET.q max_lenght 40 %}
{{ result.object.get_absolute_url }}
