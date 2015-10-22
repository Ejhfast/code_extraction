# In SQLAlchemey, Can I add new object to the relationship object?
parent = session.query(Parent).filter(Parent.id=1).first()
child = Child(parent=parent, name='child3')
session.add(child)
