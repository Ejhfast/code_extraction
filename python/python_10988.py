# Django: 'User' object has no attribute 'user'
def get_alertnum(user):
    return Alert.objects.filter(read=False, for_user=user).count()
