# In SQLAlchemy, can you filter a polymorphically associated model by the type of its associated record?
for address in sess.query(Address).join(Address.association).filter_by(type='users'):
    print "Street", address.street, "Member", address.member
