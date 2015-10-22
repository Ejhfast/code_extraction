# How to find a list of objects that do not have a relationship with another object in django
Member.objects.attribute.exclude(id=clubmember_set__member_id)
