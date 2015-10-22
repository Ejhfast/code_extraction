# Finding document based on incomplete dictionary in pymongo/MongoDB
db.appointments.find({'name': some_name, 'time.month' : mm, 'time.day': dd, 'time.year': yyyy}})
