# sqlalchemy validator for two fields
@validates('started_at', 'stopped_at')
def do_validation(self, key, field):
    return field
