# How to pass Django variable as javascript method parameter?
var user = [{% for i in user %}{{ i }}{% if forloop.last %} {%else%} , {%endif%} {% endfor %}];
