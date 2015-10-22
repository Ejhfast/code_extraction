# manual input field - value and maxlength
&lt;input id="{{ form.name.auto_id }}" type="text" name="{{ form.name.name }}" maxlength="{{ form.name.field.widget.attrs.max_length }}" value="{% if form.name.value %}{{ form.name.value }}{% endif %}"/&gt;
