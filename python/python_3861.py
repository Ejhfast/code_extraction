# sqlalchemy: one-to-one relationship with declarative
bar_id = Column(Integer, ForeignKey(Bar.id))
bar = relationship(Bar, uselist=False)
