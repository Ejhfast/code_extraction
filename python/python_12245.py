# Insert data into specific table (sqlalchemy)
engine.execute(table_addresses.insert(), name='Joe', age=20)
engine.execute(table_contacts.insert(), email='joe@something.com', cellnumber='267534320')
