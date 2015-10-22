# Django Rest Framework won't let me have more than one permission
from rest_condition import Or
...
permission_classes = (Or(permissions.IsAdminUser, TokenHasReadWriteScope))
