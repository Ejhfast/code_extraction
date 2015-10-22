# Sqlalchemy get result as KeyedTuple instead of mapped objects
&gt;&gt;&gt; user_columns = User.__table__.columns
&gt;&gt;&gt; sess.query(*user_columns).all()  # unpack user_columns into arguments
[(1, u'One', u'one@example.com', u'An address'), (2, u'Two', u'two@example.com', u'An address'), (3, u'Three', u'three@example.com', u'An address')]
