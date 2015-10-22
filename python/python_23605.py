# Sqlalchemy Foreign key relationship error while creating tables
owner_id = Column(Integer,ForeignKey('users.id'))
owner = relationship('Users',backref = 'users')
