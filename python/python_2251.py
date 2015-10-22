# Equivalent of PHP "echo something; exit();" with Python/Django?
from django.http import HttpResponse
return HttpResponse(str(var))
