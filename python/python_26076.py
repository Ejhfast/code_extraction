# Date filter in list-comphresion with class variable
userSubset = set([user for user in users for record in user.records if dt &lt; record.datetime &lt; dt + timedelta(days=7)])
