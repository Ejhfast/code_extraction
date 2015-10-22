# How to do query with `WHERE value IN list` in the Python Peewee ORM?
MyModel.select().where(MyModel.sell_currency &lt;&lt; ['BTC', 'LTC'])
