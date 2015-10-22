# Django QuerySet is too redundant
def field_by(self, field_name, user):
    return self.filter(**{field_name + '__user': user})
