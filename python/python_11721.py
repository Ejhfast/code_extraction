# Object has no attribute 'items_set'. Django orm
total = m.items.all().annotate(total=Sum('item_price'))
