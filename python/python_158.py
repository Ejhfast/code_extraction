# What is the best way to serialize a ModelForm object in Django?
{% for field in form.fields %}
    &lt;div class="form-field"&gt;{{ field }}&lt;/div&gt;
{% endfor %}
