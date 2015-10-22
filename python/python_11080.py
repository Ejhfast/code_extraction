# How to output a comma delimited list in jinja python template?
{% if not loop.last %}
    ,
{% endif %}
