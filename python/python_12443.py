# SQLAlchemy: return existing object instead of creating a new on when calling constructor
user.email = Email.as_unique('foo@bar.com')
