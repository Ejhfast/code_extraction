# How to generated xml file in Django
from django.core import serializers
data = serializers.serialize("xml", SomeModel.objects.all())
