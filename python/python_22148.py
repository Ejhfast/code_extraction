# Peewee creates mutiple records (on flask app)
for bt in list(Bet.select().where(Bet.match == m)):
