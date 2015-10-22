# How to do a .where(somecolumn == None/Null/Empty) with Peewee?
Message.select().where(Message.somecolumn &gt;&gt; None)
