# Django: reverse accessors for foreign keys clashing
create_user = models.ForeignKey(User, related_name='%(class)s_requests_created')
