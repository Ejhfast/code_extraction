# How to pass Non-essential Built-in object as parameter in django-rq enqueue
from django.models import model_to_dict
my_dict = model_to_dict(my_instance,fields=[],exclude=[])
