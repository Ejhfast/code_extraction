# How do I do this "order by" in Django, if I have foreign keys?
Ego.objects.all().select_related.order_by("auth_user.first_name")
