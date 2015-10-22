# Python sqlite3 - How do I formulate a condition where we check if an attribute in the table is one of the elements in my list
query = 'select * from test where data in ({})'.format(','.join(['?']*len(my_list)))
curr.execute(query, my_list)
