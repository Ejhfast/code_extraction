# Constant property/column value for objects in SQLAlchemy
mapper(Address, addresses_table,
            exclude_properties=['street', 'city', 'state', 'zip'])
