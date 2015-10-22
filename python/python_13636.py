# dictsort template filter and filtering with two columns
{% for item in mydict|dictsortreversed:"column1"|dictsortreversed:"column2" %}
