# flask sqlalchemy update error - update() missing 1 required positional argument: 'self'
user = User.query.get(id)
user.update(email=args.email)
