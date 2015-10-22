# Django import error when apps with same name
from django.contrib.contenttypes.models import ContentType
model_ct = ContentType.objects.get(app_label="book", model="some_model_you_gonna_import")
target_model = model_ct.model_class()
