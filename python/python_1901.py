# In Python, can I single line a for loop over iterator with an IF filter?
important_airports = (airport for airport in airports if airport.is_important)
for airport in important_airports:
    # do stuff
