# Validating for uniqueness in MongoAlchemy?
&gt;&gt;&gt; class Person(Document):
...     name = StringField()
...     name_index = Index().ascending('name').unique()
