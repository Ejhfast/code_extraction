# IN condition in Where clause on Peewee
Order.select().where(Order.statusid.in_(statuses))
