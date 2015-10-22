# Inserting tuple's elements to database
myTuple = ['a','b','c','d','e','f','g']
cur.executemany("INSERT INTO rehberim(names, phone, mobile, email, \
                    photo, address, note, date) VALUES({0}, {1}, {2}, {3}, {4}, {5}, {6}" .format (myTuple[1], myTuple[2], myTuple[3], myTuple[4], myTuple[5], myTuple[6], myTuple[7])
