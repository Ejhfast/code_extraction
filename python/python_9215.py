# Make changes persistent in Boto
query = 'select * from `DomainName` where key1=val1'
check = domain.select(query, consistent_read=True)
itemName = check.next()['key2']
