# convert class to dictionary
{ key: getattr(user, key) for key in dir(user) if not key.startswith('_') }
