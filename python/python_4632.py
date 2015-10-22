# In Zope/ZODB, how to delete objects from a BTreeFolder2
app.restrictedTraverse('/path/to/folder').manage_delObjects(list_of_ids)
transaction.commit()
