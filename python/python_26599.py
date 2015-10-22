# Get username in url [Django] [mongoengine]
def get_queryset(self):
    user = User.objects.get(username=self.kwargs['username'])
    return self.model.objects(user=user.id)
