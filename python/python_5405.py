# Creating xml file in django
from django.core import serializers
data = serializers.serialize("xml", SomeModel.objects.all())
