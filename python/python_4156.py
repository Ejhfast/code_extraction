# Trying and expand the contrib.auth.user model and add a "relationships" manage
f= Relationships.objects.filter( from_user=some_user, is_friend=True )
