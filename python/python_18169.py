# AttributeError: 'NoneType' object has no attribute 'check_password' error in django allauth
form = ChangePasswordForm(data=request.POST, user=request.user)
