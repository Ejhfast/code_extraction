# How to make generic ListView only show user's listing?
def get_queryset(self):
    return self.model.objects.filter(user=self.request.user)
