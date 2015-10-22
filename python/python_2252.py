# Is it possible to get sqlalchemy to create a composite primary key with an integer part without making it an IDENTITY type?
Column(u'int_part', Integer, primary_key=True, nullable=False,
       autoincrement=False)
