# Python protoRPC: Recursive message class
&gt;&gt;&gt; class Node(messages.Message):
...     name = messages.StringField(1)
...     children = messages.MessageField('Node',2,repeated=True)
