# Where is the best place to associate a 'form display text' with SQLAlchemy mapped property?
Class User(Base):
    name = Column(String, info={verbose_name: 'Enter your username',})
    password = Column(String, info={verbose_name: 'Enter your password',})
