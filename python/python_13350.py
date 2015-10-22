# SQLAlchemy: limit in the same string as where
results = db.session.query(User).filter(User.name == "Bob").order_by(User.age.desc()).limit(10)
