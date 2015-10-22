# Django ORM: Recursive many-to-many field join
Permission.objects.filter(Q(permission__user__id=3) | Q(user__id=3), type=1822).distinct()
