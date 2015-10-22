# Using Ancestors vs. StructuredProperty for relationships between entities
user_key = ndb.Key(User, 'some_username')
a = Achievement(parent=user_key, achievement_name='some_name')
