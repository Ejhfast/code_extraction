# How can I select all items referenced by a specific list:reference field?
item_ids = db.my_categories(slug=request.args[0]).items_
items = db(db.my_items.id.belongs(item_ids)).select()
