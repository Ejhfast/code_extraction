# How to use couchdb-python to call a view with a list of keys?
models = [d.value for d in views.models(self._db, keys=principals).rows]
