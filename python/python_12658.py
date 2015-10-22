# How to aggregate objects from a QuerySet
Comment.objects.filter(user__in=self.get_following())
