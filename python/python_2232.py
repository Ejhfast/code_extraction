# How do I list all classes of a given type in a python file?
from django.db.models.loading import get_models, get_app
app = get_app('myappname')
models = get_models(app)
