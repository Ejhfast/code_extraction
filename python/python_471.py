# Django form field using SelectDateWidget
from django.forms import extras
...
    DOB = forms.DateField(widget=extras.SelectDateWidget)
