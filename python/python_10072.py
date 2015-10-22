# django one-to-many relation
from django.contrib.auth.models import User
models.ForeignKey(Badge, null=True, blank=True).contribute_to_class(User, 'badge')
