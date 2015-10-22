# Django- How to Exclude parent class' fields
fields = [f.name for f in app1.EmployeeExtended._meta._fields() if f not in app1.Employee._meta._fields()]
