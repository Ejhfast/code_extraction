# CommandError: notifications.notification: 'recipient defines a relation with the model 'auth.User'
recipient = models.ForeignKey(User, blank=False, related_name='notifications')
