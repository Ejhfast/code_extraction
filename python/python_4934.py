# Django pagination error
{% if emp_list.has_next %}
  &lt;a href="?page={{ emp_list.next_page_number }}&amp;choices={{ val2 }}&gt;Next&lt;/a&gt;
{% endif %}
