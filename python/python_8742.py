# Django:how to access to ForeignKey's model?
from django.contrib.contenttypes.models import ContentType
model_type = ContentType.objects.get_for_model(modelA.field1)
model_type.model_class().objects.all() # this will get you all objects of the foreign key model
