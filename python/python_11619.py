# Filtering object from one model accordingly to the field of another
Customer.filter(id__in = [nsu.pk for nsu in NewSecUser.all()]).filter(is_visible_on_new_selection=True).all()`
