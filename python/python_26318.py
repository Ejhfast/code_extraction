# Django Rest Framework add field to model before saving in viewset using ModelSerializer
def perform_create(self, serializer):
    serializer.save(user=self.request.user)
