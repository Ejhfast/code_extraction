# Simple way to delete users account?
user = User.objects.get(username='their_username')
user.delete()
