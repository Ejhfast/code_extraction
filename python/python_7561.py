# How can I order a queryset by a filtered bridge table field?
qs = user.blog_set.all().order_by("follow__created")
