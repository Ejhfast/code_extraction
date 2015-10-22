# Can I filter users to require a matching entry on every date in a given range?
employees = Employee.objects.all()
for day in range(19, 26):
    employees = employees.filter(shift__date_requested=datetime.date(2015, 7, day))
