# How to save a model without sending a signal?
user_id = 142187
User.objects.filter(id=user_id).update(name='tom')
