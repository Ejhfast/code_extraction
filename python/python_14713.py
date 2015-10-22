# A django like unique together in turbogears/sqlalchemy
class ShoppingList(Base):
    thing1_id = Column(Integer, primary_key=True)
    thing2_id = Column(Integer, primary_key=True)
