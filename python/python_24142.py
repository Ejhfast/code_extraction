# how to select with if statement by peewee
Category.select(Category, ItemCategory, fn.IF(ItemCategory.category_id==None, 0, 1) )
