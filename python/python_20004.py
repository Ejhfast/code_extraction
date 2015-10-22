# user=request.user - name 'request' is not defined
def get_queryset(self):
    return Fruit.objects.filter(user=self.request.user)
