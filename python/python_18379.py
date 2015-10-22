# Trying to filter by field value with django database API
o = Message.objects.filter(in_reply_to_id__gt=0)
