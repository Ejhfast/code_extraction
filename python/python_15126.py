# How to get column names of a schema in sqlsoup in python?
&gt;&gt;&gt; messages = Table('messages', meta, autoload=True, autoload_with=engine)
&gt;&gt;&gt; [c.name for c in messages.columns]
['message_id', 'message_name', 'date']
