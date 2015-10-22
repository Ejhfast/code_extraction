# How can I access self referential property in sqlalchemy?
class Employee(Base):
    ...
    manager = relationship("Employee", remote_side=[id])
