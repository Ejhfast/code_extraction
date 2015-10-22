# Override get_object() and manually set PK
def get_object(self):
    return self.model.get(pk=self.request.user.pk)
