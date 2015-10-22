# how to rewrite a url and change it from database values in django
def idDetailIndex(request, user_id):
    user = User.objects.get(id=user_id)
    return redirect('FLSocial', first_name=user.firstName, last_name=user.lastName)
