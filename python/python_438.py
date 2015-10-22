# Testing time sensitive applications in Python
def is_expired(self, check_date=None):
    _check_date = check_date or datetime.utcnow()
    return self.create_date + timedelta(days=15) &lt; _check_date
