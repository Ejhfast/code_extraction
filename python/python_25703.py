# Django - retrieve form data
from django.http import QueryDict
d = QueryDict(request.POST['form'])
role = d['role']
