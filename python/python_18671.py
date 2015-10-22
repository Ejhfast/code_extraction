# How to use django-avatar with my own User model and not with django.contrib.auth.models.User
66. class Avatar(models.Model):
67.     user = models.ForeignKey(getattr(settings, 'AUTH_USER_MODEL', 'auth.User'))
68.     ....
