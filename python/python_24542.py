# how can we apply conditions on joined table in Django..?
queryset.filter(Q(from_user_id=from_user_id,deleteFlag=deleteFlag) | Q(to_user_id=to_user_id,deleteFlag=deleteFlag)).exclude(to_user_status=3)
