# Handle a request header in Django rest framework to get the secret key passed in the header?
class MyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print self.request.META.get('HTTP_SECRET_KEY', None)
