# How do I retrieve a Django model class dynamically?
from django.db.models.loading import get_model
model = get_model('app_name', 'model_name')
