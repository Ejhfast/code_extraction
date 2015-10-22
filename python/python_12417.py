# How to index elements of a tuple in Django template using a variable?
{% for week_info in week_infos %}
    &lt;td row="{{ forloop.counter0 }}" col="{{ i|add:6 }}"&gt;
        {{ week_info }}
