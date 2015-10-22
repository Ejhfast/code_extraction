# SQLAlchemy: .label() an addition of values
session.query((Person.age + Person.wealth).label("lbl"))
