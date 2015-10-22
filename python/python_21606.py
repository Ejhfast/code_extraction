# Can an object method return an instance of the object?
@classmethod
def from_user(cls, user):
    return cls.objects.get(username=user.username)
