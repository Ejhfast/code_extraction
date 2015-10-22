# Get last_login time for a certain user? (django)
user = User.objects.get(username='user1')
last_login = user.last_login
