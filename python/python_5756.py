# Django query across many-to-many relationship
Target.objects.filter( store__user_profile__user=request.user )
