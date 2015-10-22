# how to hash password with a basic sign in form in django with mongoengine?
user = User(username=username, email=email)
user.set_password(password)
user.save()
