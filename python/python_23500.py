# Operator NOT IN with Peewee
Tweet.select().where(~(Tweet.user &lt;&lt; a_users))
