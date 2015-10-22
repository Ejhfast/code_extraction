# Django REST Custom Errors
return Response({'detail' : "Invalid arguments", 'args' : ['arg1', 'arg2']},
                     status = status.HTTP_400_BAD_REQUEST)
