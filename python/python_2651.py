# Pylons + SQLAlchemy problem: The transaction is inactive due to a rollback in a subtransaction
def __before__(self):
    model.Session.close()
