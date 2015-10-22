# Django: exclude User list from all Users
def get_other_users(self):
    return User.objects.exclude(assign__shift=self)
