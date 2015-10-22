# Django generic login view return 'str object not callable' error
from testapp.forms import UsersForm
url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'testapp/templates/login.html', 'authentication_form':UsersForm}),
