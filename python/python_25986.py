# How to remove an entity from structured property - python GAE?
guido = Contact.query(Contact.name == 'Guido').get()
guido.addresses = [i for i in guido.addresses if i.type != 'work']
guido.put()
