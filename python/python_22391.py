# How to create a mixin pattern in Python
def get_queryset(self, *args, **kwargs)
    user = self.request.user
    return super(UserListMixin, self).get_queryset(*args, **kwargs).filter(user=user)
