# DRF permission not taking effect
permission_classes = [And(Or(permissions.IsAdminUser, TokenHasReadWriteScope), IsOwnerOrReadOnly)]
